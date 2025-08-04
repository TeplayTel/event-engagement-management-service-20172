"""
MongoDB interaction logic for events.
"""

from src.constants.app_constants import COLLECTION_EVENTS
from src.logging.logger import get_logger
from pymongo.collection import Collection
from typing import Optional, Dict

# PUBLIC_INTERFACE
class EventRepository:
    """
    Handles all DB operations for events.
    """
    def __init__(self, db):
        """
        Initializes with the MongoDB database reference.
        Args:
            db: The MongoDB client database instance.
        """
        self.db = db
        self.collection: Collection = self.db[COLLECTION_EVENTS]
        self.logger = get_logger(self.__class__.__name__)

    # PUBLIC_INTERFACE
    def insert_event(self, event_data: dict) -> Optional[str]:
        """
        Insert event record (expects snake_case keys).
        Args:
            event_data: dict using snake_case keys.
        Returns:
            The inserted event's ID (str), or None if insertion failed.
        """
        try:
            result = self.collection.insert_one(event_data)
            inserted_id = str(result.inserted_id)
            self.logger.info(f"Inserted event with id={inserted_id}")
            return inserted_id
        except Exception as exc:
            self.logger.error(f"Failed to insert event: {exc}")
            return None

    # PUBLIC_INTERFACE
    def find_event(self, event_id: str) -> Optional[Dict]:
        """
        Find event by ID.
        Args:
            event_id: Event MongoDB document _id value as string.
        Returns:
            Event document (dict) if found, else None.
        """
        from bson.objectid import ObjectId
        try:
            record = self.collection.find_one({"_id": ObjectId(event_id)})
            self.logger.debug(f"find_event(event_id={event_id}) found={record is not None}")
            return record
        except Exception as exc:
            self.logger.warning(f"Error in find_event: {exc}")
            return None

    # PUBLIC_INTERFACE
    def update_event_status(self, event_id: str, new_status: str) -> bool:
        """
        Updates the status of an event by ID.
        Args:
            event_id: Event MongoDB document _id value as string.
            new_status: The updated status string.
        Returns:
            True if update applied, False if not.
        """
        from bson.objectid import ObjectId
        try:
            res = self.collection.update_one(
                {"_id": ObjectId(event_id)},
                {"$set": {"status": new_status}}
            )
            if res.modified_count:
                self.logger.info(f"Updated event={event_id} status={new_status}")
            return res.modified_count > 0
        except Exception as exc:
            self.logger.error(f"Failed to update event status: {exc}")
            return False
