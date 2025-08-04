"""
Pydantic schemas for event timeline requests and responses.
"""

from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class EventTimelineRecord(BaseModel):
    """Schema for a single timeline record."""
    event_id: str = Field(..., description="Parent event ID")
    # Add fields for time, action, status, logs, etc.
