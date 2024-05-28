from typing import Optional, Union
from pydantic import BaseModel


class Token(BaseModel):
    """
    Represents ERC20 token
    """
    address: str
    name: str
    symbol: str
    decimals: int
    price: Union[str, float]
    imageUrl: Optional[str] = None
    valuable: Optional[bool] = None
    verified: bool
    category: Optional[str] = None

