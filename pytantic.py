from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple, Set
from pydantic import BaseModel


class Book(BaseModel):
    name: str = "Lista Telefonica"
    price: float = 10.00
    year: datetime


book1 = {"name": "book1", "price": 11.11, "year": datetime.now()}

book_object = Book(**book1)

# print(book_object.price)
print("------")
# print(book_object.year)
print(book_object)
print("------")
