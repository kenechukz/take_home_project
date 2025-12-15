"""
FastAPI application entry point for Interaction Tracker
"""

from fastapi import FastAPI, HTTPException
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


# Import and include routers
# TODO: Add your interaction routes here
#from src.routes import interactions
# app.include_router(interactions.router, prefix="/api")
