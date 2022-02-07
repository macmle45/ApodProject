from datetime import date
from pydantic import BaseModel


class ApodData(BaseModel):
    apod_date: date
    title: str
    media: bytes
    description: str
    copyright: str
