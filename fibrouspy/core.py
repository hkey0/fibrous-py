import enum
from typing import List, Dict

import requests

from models import RouteSuccess, Token, Protocol, RouteParams
from utils import build_route_url


class FibrousClient:
    """
    A client to interact with the Fibrous API.


    Args:
        route_url (str): The base URL for the route API.
        graph_url (str): The base URL for the graph API.
        router_address (str): The address of the fibrous router.
    """
    def __init__(self, route_url: str = "https://api.fibrous.finance",
                 graph_url: str = "https://graph.fibrous.finance",
                 router_address: str =
                 "0x00f6f4CF62E3C010E0aC2451cC7807b5eEc19a40b0FaaCd00CCA3914280FDf5a"
                 ) -> None:
        self.route_url = route_url
        self.graph_url =graph_url
        self.router_address = router_address
        self.headers = {"User-Agent": "FibrousPy/0.1.0"}

    def supported_tokens(self) -> Dict[str, Token]:
        """
        A list of supported tokens by Fibrous.


        Returns:
            tokens (List[Token]): Tokens list.

        """
        response = requests.get(f"{self.graph_url}/tokens",
                                headers=self.headers).json()
        print("get")
        tokens: Dict[str, Token] = {}
        for item in response:
            tokens[item["symbol"].lower()] = Token(**item)

        return tokens

    def supported_protocols(self) -> Dict[str, Protocol]:
        """
        A list of supported AMM protocols by Fibrous.

        Returns:
            protocls (Dict[str, Protocol]): List of protocols.
        """
        response = requests.get(f"{self.route_url}/protocols",
                                headers = self.headers).json()
        protocols = {}
        for i, v in enumerate(response):
            protocols[v] = Protocol(i)

        return protocols

    def get_best_route(self, amount: int, token_in_address: str,
                       token_out_address: str):
        """
        Get best route and extra data from Fibrous Router.


        Args:
            amount (in): Amount of tokens to be swapped.
            token_in_address (str): Input token address.
            token_out_address (str): Output token address.

        Returns:
            route_response (RouteSuccess): Detailed route response.
        """
        route_params = RouteParams(amount=amount,
                                   tokenInAddress=token_in_address,
                                   tokenOutAddress=token_out_address)
        route_url = build_route_url(f"{self.route_url}/route", route_params)

        response = requests.get(route_url, headers=self.headers).json()
        route_response = RouteSuccess(**response)

        return route_response



api = FibrousClient()
data = api.get_best_route(100000000000, "0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7", "0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8")
# data = api.supported_tokens()

print("cwboolok")
print(data.outputToken)



