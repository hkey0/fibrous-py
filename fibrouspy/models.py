from enum import Enum
from typing import List, Any, Optional, Dict
from dataclasses import dataclass

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


class Protocol(Enum):
    MYSWAP = 0
    JEDISWAP = 1
    TENKSWAP = 2
    SITHSWAP = 3
    EKUBO = 4
    MYSWAPCL = 5
    STARKDEFI = 6
    JEDISWAPCL = 7
    NOSTRA = 8
    HAIKO = 9


class RouteParams(BaseModel):
    amount: int
    tokenInAddress: str
    tokenOutAddress: str


class Swap(BaseModel):
    protocol: int
    poolId: str
    poolAddress: str
    fromTokenAddress: str
    toTokenAddress: str
    percent: str


class Route(BaseModel):
    percent: str
    swaps: List[List[Swap]]


class RouteSuccess(BaseModel):
    success: bool
    inputToken: Token
    inputAmount: str
    outputToken: Token
    outputAmount: str
    route: List[Route]
    estimatedGasUsed: str
    bestQuotesByProtocols: List[str]
    time: float
    initial: bool

