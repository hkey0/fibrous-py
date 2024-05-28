import requests


class FibrousClient:
    def __init__(self, route_url: str = "https://api.fibrous.finance",
                 graph_url: str = "https://graph.fibrous.finance",
                 router_address: str =
                 "0x00f6f4CF62E3C010E0aC2451cC7807b5eEc19a40b0FaaCd00CCA3914280FDf5a"
                 ) -> None:
        self.route_url = route_url
        self.graph_url =graph_url
        self.router_address = router_address
        
