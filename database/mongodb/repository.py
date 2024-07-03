import os
import pymongo
from bson.json_util import dumps


MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")
MONGO_USER = os.environ.get("MONGO_USER", "admin")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "Abc12345")

mongo_client = pymongo.MongoClient(
    f"mongodb+srv://huutai1515225:Huutai234@cluster0.kus9noc.mongodb.net/"
)
