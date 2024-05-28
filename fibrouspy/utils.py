from typing import List, Union
from urllib.parse import urlencode

from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.client_models import Call

from .models import RouteParams, RouteExecuteParams


def build_route_url(url: str, route_params: RouteParams | RouteExecuteParams) -> str:
    params = urlencode(route_params.__dict__)
    return f"{url}?{params}"


def fix_calldata(calldata: List[Union[str, int]]) -> List[int]:
    def convert(d: Union[str, int]) -> int:
        if isinstance(d, str):
            return int(d, 16) if d.startswith("0x") else int(d)
        return d

    return [convert(d) for d in calldata]


def build_approve_call(token_address: str, amount: int) -> Call:
    approve_call = Call(
        to_addr=int(token_address, 16),
        selector=get_selector_from_name("approve"),
        calldata=[
            # spender -> fibrous router
            0x00f6f4CF62E3C010E0aC2451cC7807b5eEc19a40b0FaaCd00CCA3914280FDf5a,
            amount,
            0x0
    ])
    return approve_call

