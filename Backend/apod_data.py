import datetime
from pydantic import BaseModel


class ApodData(BaseModel):
    date: datetime
    title: str
    media: bytes
    description: str
    copyright: str
