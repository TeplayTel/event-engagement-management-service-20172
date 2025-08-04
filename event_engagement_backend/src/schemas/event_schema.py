"""
Pydantic schemas for event requests and responses.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# PUBLIC_INTERFACE
class EventCreateRequest(BaseModel):
    """
    Schema for creating an event (API request body).
    """
    name: str = Field(..., description="Event name")
    description: Optional[str] = Field(None, description="Description of the event")
    owner_id: Optional[str] = Field(None, description="Owner/creator user ID")
    # More fields (time, tags, etc.) can be added as needed.


# PUBLIC_INTERFACE
class EventResponse(BaseModel):
    """
    Schema for returning event details in API responses.
    """
    id: str = Field(..., description="Event ID")
    name: str = Field(..., description="Event name")
    description: Optional[str] = Field(None, description="Description of the event")
    owner_id: Optional[str] = Field(None, description="Owner/creator user ID")
    status: str = Field(..., description="Event status")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
