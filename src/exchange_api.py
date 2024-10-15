import aiohttp
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def get_btc_binance_price(request: Request) -> Response:
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            # return web.Response(text=data['price'])
            return web.json_response(data)


async def get_eth_binance_price(request: Request) -> Response:
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            # return web.Response(text=data['price'])
            return web.json_response(data)


async def get_pepe_binance_price(request: Request) -> Response:
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=PEPEUSDT'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            # return web.Response(text=data['price'])
            return web.json_response(data)
