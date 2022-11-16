import datetime as dt
from pymongo import MongoClient

from radar_mongodb import QueryManager

class APILayer:
    def __init__(
        self,
        mongodb_uri: str,
        cboe_collection_name: str = None,
        spot_collection_name: str = None,
        open_interest_collection_name: str = None
    ):
        self.query_manager = QueryManager(
            MongoClient(mongodb_uri).get_default_database(),
            cboe_collection_name,
            spot_collection_name,
            open_interest_collection_name
        )

    def find(self, date: dt.date):
        return self.query_manager.spot_queries.find(date)