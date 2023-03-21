from pydantic import BaseModel
from typing import List
from datetime import datetime


class OnTrackBaseModel(BaseModel):
    id: str
    archive: bool = False
    create_time: datetime = datetime.now()
    update_time: datetime = datetime.now()


class OnTrackUpdateBaseModel(BaseModel):
    id: str
    update_time: datetime = datetime.now()


class OnTrackIdBaseModelList(BaseModel):
    ids: List[str]


class OnTrackUpdateResponseBaseModel(BaseModel):
    modified_count: int
