from dataclasses import dataclass


@dataclass
class Token:
    address: str
    name: str
    symbol: str
    decimals: int
    price: str
    image_url: str
    valuable: bool
    verified: bool
