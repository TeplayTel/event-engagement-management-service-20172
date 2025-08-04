"""
Event domain model(s).
"""

from enum import Enum
from datetime import datetime
from typing import Optional


# PUBLIC_INTERFACE
class EventStatus(Enum):
    """Enum representing event status state transitions."""
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


# PUBLIC_INTERFACE
class Event:
    """
    Business model representing a fan engagement event.

    Attributes follow camelCase convention for POJO usage.
    """
    def __init__(
        self,
        eventId: str,
        name: str,
        description: Optional[str] = None,
        ownerId: Optional[str] = None,
        status: str = EventStatus.CREATED.value,
        createdAt: Optional[datetime] = None,
        updatedAt: Optional[datetime] = None,
    ):
        self.eventId = eventId
        self.name = name
        self.description = description
        self.ownerId = ownerId
        self.status = status
        self.createdAt = createdAt or datetime.utcnow()
        self.updatedAt = updatedAt or datetime.utcnow()
