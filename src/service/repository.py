from typing import List
from pydantic import BaseModel
from database.mongodb.repository import mongo_client



class Event(BaseModel):
    eventID: str
    eventIntro:str
    startDate:str
    endDate:str
    location:str
    eventTypeID :str
    eventDescription:str
    eventOrganizationID:str
    picture:str
class EventType(BaseModel):
    eventTypeID:str
    eventTypeName:str
    eventTypeDescription:str
        
def getEvents():
    try:
        db = mongo_client["event-service"]
        collection = db["events"]
        result = list(collection.find({}, {"_id": 0}))
        return result
    except Exception as e:
        return {"error": str(e)}
def getEventsType():
    try:
        db = mongo_client["event-service"]
        collection = db["event-type"]
        result = list(collection.find({}, {"_id": 0}))
        return result
    except Exception as e:
        return {"error": str(e)}

def getEventbyID(eventid: str):
    try:
        db = mongo_client["event-service"]
        collection = db["events"]
        condition = {"eventID": eventid}
        result = collection.find_one(condition, {"_id": 0})
        if result:
            return result
        else:
            return {"error": "Event not found"}
    except Exception as e:
        return {"error": str(e)}


def getEventbyType(event_types: List[str]):
    try:
        db = mongo_client["event-service"]
        collection = db["events"]
        cursor = collection.find({"eventTypeID": {"$in": event_types}}, {"_id": 0})
        events = list(cursor)
        return events
    except Exception as e:
        return {"error": str(e)}


def createEvent(event):
    try:
        db = mongo_client["event-service"]
        collection = db["events"]
        collection.insert_one(event)
        return {"status": "success", "message": "Event created successfully"}
    except Exception as e:
        return {"error": str(e)}

def createEventType(eventType):
    try:
        db = mongo_client["event-service"]
        collection = db["events"]
        collection.insert_one(eventType.dict())
        return {"status": "success", "message": "Event created successfully"}
    except Exception as e:
        return {"error": str(e)}       

def updateEvent(id:str, event:Event):
    try:
        db = mongo_client["event-service"]
        collection = db["events"]
        result = collection.find_one_and_update(
            {"eventID": id},
            {"$set": event.dict()},
            upsert=True,
            return_document=True
        )

        if result:
            return {"status": "updated", "eventID": id}
        else:
            return {"status": "created", "eventID": id}

    except Exception as e:
        return {"error": str(e)}

def deleteEvent(id:str):
    try:
        db = mongo_client["event-service"]
        collection = db["events"]
        result = collection.delete_one({"eventID": id})
        if result.deleted_count > 0:
            return {"status": "success", "message": f"Event {id} deleted successfully"}
        else:
            return {"status": "not found", "message": f"Event {id} not found"}
    except Exception as e:
        return {"error": str(e)}

