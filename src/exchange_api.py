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


async def pub_ssh_key(request: Request) -> Response:
    return web.Response(text='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDmhlK8AFyvhqPRBxMq+GYudWrqYnQah5hpg0zOH7/eKy0+OG1+VjuQCjixPqC7qrRuIv5NrvNjdSOa/fqelRg4ucjbYT2IsphbINosC9FdaDAJkm7FVSxxrpgMx/vGvWpdwgn01ixV1MLrIVeSbOIMMbtssgInrLA37rCJdv7xF5sqzeiF/sIU7Ixas4igAnqTnKTqm2F3LAYoLAhZ8KNeLERrY/MtCNRLFI6rR15fAFQrCG0a8lyOOr20UVrYpHNs+in4ky1RJqJVmmvPuj88y6KgEb13UU8bKvrzvzBOEM8y7yKj8ST57WPPa+9BhYoyMwXSisvriYZIK3E3Y7J utah@MacBook-Pro-Aleksej.local')
