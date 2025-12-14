"""
FastAPI application entry point for Interaction Tracker
"""

from fastapi import FastAPI
from routes import interactions
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI(
    title="Interaction Tracker API",
    description="API for tracking user interactions",
    version="1.0.0"
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


# Import and include routers
# TODO: Add your interaction routes here
#from src.routes import interactions
# app.include_router(interactions.router, prefix="/api")
