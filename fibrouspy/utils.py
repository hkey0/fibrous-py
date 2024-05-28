from dataclasses import dataclass
from urllib.parse import urlencode

from models import RouteParams


def build_route_url(url: str, route_params: RouteParams) -> str:
    params = urlencode(route_params.__dict__)
    return f"{url}?{params}"
