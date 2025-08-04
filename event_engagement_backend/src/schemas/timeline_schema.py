"""
Pydantic schemas for event timeline requests and responses.
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

# PUBLIC_INTERFACE
class EventTimelineRecord(BaseModel):
    """
    Schema for a single timeline record (used for recording entries in the timeline).
    """
    event_id: str = Field(..., description="Parent event ID (links to event)")
    action: str = Field(..., description="Action type (started, updated, completed, aborted)")
    timestamp: datetime = Field(..., description="Time of timeline action")
    status: str = Field(..., description="Status at this timeline step (pending, in_progress, completed, failed)")
    details: Optional[Dict] = Field(None, description="Optional details associated with this timeline log")
    logs: Optional[str] = Field(None, description="Text log for this entry")
