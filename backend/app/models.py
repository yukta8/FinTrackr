from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import date

class Transaction(SQLModel,table=True):
    __tablename__ = "transactions" # bcs transaction keyword reserved
    id: Optional[int] = Field(default=None, primary_key= True)
    tx_date: date
    amount: float
    merchant: str
    raw_description: str
    category: str
