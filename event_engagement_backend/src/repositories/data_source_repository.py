"""
MongoDB interaction logic for data source configs.
"""

from src.constants.app_constants import COLLECTION_DATA_SOURCES
from src.logging.logger import get_logger
from pymongo.collection import Collection
from typing import Optional, Dict

# PUBLIC_INTERFACE
class DataSourceRepository:
    """
    Handles DB persistence for data source configs.
    """

    def __init__(self, db):
        """
        Initializes the repository with a MongoDB database reference.
        Args:
            db: The MongoDB client database instance.
        """
        self.db = db
        self.collection: Collection = self.db[COLLECTION_DATA_SOURCES]
        self.logger = get_logger(self.__class__.__name__)

    # PUBLIC_INTERFACE
    def insert_config(self, config_data: dict) -> Optional[str]:
        """
        Inserts a configuration record into the event_data_source collection.
        Args:
            config_data: Dictionary using snake_case keys representing the data source config.

        Returns:
            The inserted config's ID, or None on failure.
        """
        try:
            result = self.collection.insert_one(config_data)
            inserted_id = str(result.inserted_id)
            self.logger.info(f"Inserted data source config with id={inserted_id}")
            return inserted_id
        except Exception as exc:
            self.logger.error(f"Failed to insert config: {exc}")
            return None

    # PUBLIC_INTERFACE
    def find_config_by_id(self, config_id: str) -> Optional[Dict]:
        """
        Retrieves a data source config by its ID.

        Args:
            config_id: MongoDB document ID (string).
        Returns:
            Config document as dict or None if not found.
        """
        from bson.objectid import ObjectId
        try:
            record = self.collection.find_one({"_id": ObjectId(config_id)})
            self.logger.debug(f"Lookup config_id={config_id} found={record is not None}")
            return record
        except Exception as exc:
            self.logger.warning(f"Error in find_config_by_id: {exc}")
            return None

    # PUBLIC_INTERFACE
    def update_config(self, config_id: str, update_fields: dict) -> bool:
        """
        Updates a data source config.
        Args:
            config_id: The ID (str) of the config.
            update_fields: Dict (snake_case) of fields to update.
        Returns:
            True if update successful, False otherwise.
        """
        from bson.objectid import ObjectId
        try:
            res = self.collection.update_one(
                {"_id": ObjectId(config_id)},
                {"$set": update_fields}
            )
            if res.modified_count:
                self.logger.info(f"Updated config id={config_id} fields={list(update_fields.keys())}")
            return res.modified_count > 0
        except Exception as exc:
            self.logger.error(f"Failed to update config: {exc}")
            return False
