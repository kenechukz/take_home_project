"""
FastAPI application entry point for Interaction Tracker
"""

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR
import logging
from src.routes import interactions
from fastapi.middleware.cors import CORSMiddleware
from src.db import lifespan
from src.db import db

# Create FastAPI app instance
app = FastAPI(
    title="Interaction Tracker API",
    description="API for tracking user interactions",
    version="1.0.0",
    lifespan=lifespan
)
app.include_router(interactions.router, prefix="/api")

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Interaction Tracker API is running"}


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "interaction-tracker-api"
    }


@app.get("/db/health")
async def db_health():
    """Checks DB connectivity via a lightweight query."""
    try:
        # If the table doesn't exist yet, this will raise
        await db.interaction.count()
        return {"db": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB check failed: {e}")


# ---- Exception handlers ----
logger = logging.getLogger("interaction-tracker")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "ValidationError",
            "detail": exc.errors(),
        },
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error while processing request: %s %s", request.method, request.url)
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "InternalServerError",
            "detail": str(exc),
        },
    )

