from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.event_routes import router as event_router
from src.api.routes.data_source_routes import router as data_source_router
from src.api.routes.timeline_routes import router as timeline_router

from src.logging.logger import get_logger

app = FastAPI(
    title="Event Engagement Backend",
    description="APIs for managing fan engagement events, data sources, and timelines.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes for all resource groups
app.include_router(event_router)
app.include_router(data_source_router)
app.include_router(timeline_router)

logger = get_logger()

@app.get("/")
def health_check():
    """
    Health check endpoint. Returns app health status.
    """
    logger.debug("Health check endpoint called.")
    return {"message": "Healthy"}
