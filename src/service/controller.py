from typing import List
import uuid
from fastapi import APIRouter, Query, UploadFile
from . import repository
from pathlib import Path

router = APIRouter()
import os
from pydantic import BaseModel


UPLOAD_DIR = Path().resolve() / "upload"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)



class Event(BaseModel):
    eventID: str
    eventIntro:str
    startDate:str
    endDate:str
    location:str
    eventTypeID:str
    eventDescription:str
    eventOrganizationID:str
    picture:str
class EventType(BaseModel):
    eventTypeID:str
    eventTypeName:str
    eventTypeDescription:str
      
@router.get("/events/", response_model=list[dict])
async def event():
    events = repository.getEvents()
    return events

@router.get("/event-type/", response_model=list[dict])
async def event():
    eventType = repository.getEventsType()
    return eventType
@router.get("/event/{id}", response_model=list[dict])
async def event(id: str):
    event=repository.getEventbyID(id)
    return event
from fastapi.encoders import jsonable_encoder

@router.get("/events/type", response_model=List[Event])
async def get_events(eventTypes: List[str] = Query(...)):
    events = repository.getEventbyType(eventTypes)
    return events

@router.post("/create-event/")
async def event(data: Event):
    if data.eventID=="" or data.eventID is None:
        data.eventID = str(uuid.uuid4())
    data_to_save = jsonable_encoder(data)
    # picture= await data.picture.read()
    # data = await file_upload.read()
    # save_to = UPLOAD_DIR / file_upload.filename
    # with open(os.path.join(save_to), "wb") as f:
    #     f.write(data)
    # repository.embedding(
    #     repository.get_format(save_to)["split_name"][1], save_to, index_name
    # )
    # print(repository.get_format(save_to)["split_name"][1])
    # return {"filenames": file_upload.filename}
    return repository.createEvent(data_to_save)

@router.post("/create-eventType/")
async def event(data: EventType):
    if data.eventID=="" or data.eventID is None:
        data.eventID = str(uuid.uuid4())
    data_to_save = jsonable_encoder(data)

    return repository.createEventType(data_to_save)

@router.post("/update-event/{id}")
async def event(id:str,data: Event):    
    data_to_save = jsonable_encoder(data)
    return  repository.updateEvent(id,data_to_save)


@router.delete("/event/{id}")
async def event(id:str):
    return repository.deleteEvent(id)



