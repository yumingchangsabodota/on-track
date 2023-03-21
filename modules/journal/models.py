from typing import List
from datetime import datetime
from pydantic import BaseModel

from lib.model import OnTrackBaseModel, OnTrackUpdateBaseModel, OnTrackIdBaseModelList


class JournalEntry(OnTrackBaseModel):
    description: str
    entry_type: str  # debit or credit; debit = + , credit = -
    amount: float
    currency: str
    currency_rate: float
    amount_ntd: float
    entry_datetime: datetime = datetime.now()
    user: str


class JournalEntryList(BaseModel):
    journal_entry_list: List[JournalEntry]


class JournalEntryUpdate(OnTrackUpdateBaseModel):
    description: str
    entry_type: str  # debit or credit; debit = + , credit = -
    amount: float
    currency: str
    currency_rate: float
    amount_ntd: float
    entry_datetime: datetime
    user: str


class JournalEntryUpdateList(BaseModel):
    journal_entry_list: List[JournalEntryUpdate]
