from pydantic import BaseModel
from models.author import Author
from datetime import datetime


class Book(BaseModel):
    isbn: str
    name: str
    author: Author
    year: datetime.now()
