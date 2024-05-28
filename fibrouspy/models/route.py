from typing import List
from pydantic import BaseModel
from .token import Token

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


class RouteExecuteParams(BaseModel):
    amount: str
    tokenInAddress: str
    tokenOutAddress: str
    slippage: float
    destination: str
