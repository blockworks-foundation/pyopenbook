import asyncio
import json
import pathlib
from pyserum.market import AsyncMarket
from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey


async def main():
    ids = json.load(open(pathlib.Path(__file__).parent / 'ids.json'))

    group = [group for group in ids['groups'] if group['publicKey'] == '78b8f4cGCwmZ9ysPFMWLaLTkkaYnUjwMJYStWe5RTSSX'][0]

    connection = AsyncClient('https://mango.rpcpool.com/0f9acc0d45173b51bf7d7e09c1e5')

    serum_markets = await asyncio.gather(*[
        AsyncMarket.load(connection, PublicKey(serum_market_config['serumMarketExternal']), PublicKey(serum_market_config['serumProgram']))
        for serum_market_config in group['serum3Markets']
    ])

    serum_market: AsyncMarket = serum_markets[0]

    fills = await serum_market.load_fills(9999)

    print([fill._asdict() for fill in fills])


if __name__ == '__main__':
    asyncio.run(main())