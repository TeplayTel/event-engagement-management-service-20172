"""
MongoDB interaction logic for event timelines.
"""

from src.constants.app_constants import COLLECTION_TIMELINES
from src.logging.logger import get_logger
from pymongo.collection import Collection
from typing import Optional

# PUBLIC_INTERFACE
class TimelineRepository:
    """
    Handles DB persistence for event timelines.
    """
    def __init__(self, db):
        """
        Initializes repository with DB instance.
        Args:
            db: The MongoDB client database instance.
        """
        self.db = db
        self.collection: Collection = self.db[COLLECTION_TIMELINES]
        self.logger = get_logger(self.__class__.__name__)

    # PUBLIC_INTERFACE
    def insert_record(self, timeline_data: dict) -> Optional[str]:
        """
        Insert timeline record.
        Args:
            timeline_data: dict using snake_case keys.
        Returns:
            The inserted timeline record's ID (str), or None if error.
        """
        try:
            result = self.collection.insert_one(timeline_data)
            inserted_id = str(result.inserted_id)
            self.logger.info(f"Inserted timeline record id={inserted_id} for event_id={timeline_data.get('event_id')}")
            return inserted_id
        except Exception as exc:
            self.logger.error(f"Failed to insert timeline record: {exc}")
            return None

    # PUBLIC_INTERFACE
    def get_event_timelines(self, event_id: str) -> list:
        """
        Retrieves all timeline records for a given event_id.

        Args:
            event_id: The parent event ID.
        Returns:
            A list of timeline records (possibly empty).
        """
        try:
            docs = list(self.collection.find({"event_id": event_id}))
            self.logger.debug(f"Found {len(docs)} timelines for event_id={event_id}")
            return docs
        except Exception as exc:
            self.logger.warning(f"Error fetching timelines for event_id={event_id}: {exc}")
            return []
