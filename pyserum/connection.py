from solana.rpc.api import Client as conn  # pylint: disable=unused-import # noqa:F401
from solana.rpc.providers.http import requests

from .market.types import MarketInfo


def get_live_markets():
    url = "https://raw.githubusercontent.com/project-serum/serum-js/master/src/markets.json"
    return [
        MarketInfo(name=m["name"], address=m["address"], program_id=m["programId"])
        for m in requests.get(url).json()
        if not m["deprecated"]
    ]
