import os
import pymongo
import pandas as pd
from bson.json_util import dumps


MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")
MONGO_USER = os.environ.get("MONGO_USER", "admin")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "Abc12345")

mongo_client = pymongo.MongoClient(
    f"mongodb://localhost:27017"
)
