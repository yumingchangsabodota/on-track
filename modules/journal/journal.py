
from typing import List

from fastapi import APIRouter
from .handler import JournalEntryHandler
from .models import JournalEntry, JournalEntryList, JournalEntryUpdateList
from lib.model import OnTrackIdBaseModelList, OnTrackUpdateResponseBaseModel

router = APIRouter()


@router.post("/add", summary="Add journal entry", tags=["Journal"], response_model=OnTrackIdBaseModelList)
async def add_journal(journals: JournalEntryList) -> OnTrackIdBaseModelList:
    handler = JournalEntryHandler()
    journals = journals.dict()['journal_entry_list']
    result_ids = handler.create(journals)
    return {"ids": result_ids}


@router.get("/", summary="Get journal entry", tags=["Journal"], response_model=JournalEntryList)
async def get_journal() -> JournalEntryList:
    handler = JournalEntryHandler()
    journals = handler.get()
    return {"journal_entry_list": journals}


@router.put("/update", summary="Update assets", tags=["Asset"], response_model=OnTrackUpdateResponseBaseModel)
async def update_journal(assets: JournalEntryUpdateList) -> int:
    handler = JournalEntryHandler()
    journals = assets.dict()['journal_entry_list']
    modified_count = handler.update(journals)
    return modified_count
