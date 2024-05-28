from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    address: str
    name: str
    symbol: str
    decimals: int
    price: str | float
    imageUrl: Optional[str] = None
    valuable: Optional[bool] = None
    verified: bool
    category: Optional[str] = None

