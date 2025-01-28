from src.exchange_api import (
    get_btc_binance_price,
    get_eth_binance_price,
    get_pepe_binance_price,
    pub_ssh_key
)
from src.observability import status
from aiohttp import web
from aiohttp.web_app import Application


def setup_routes(app: Application, version: str) -> None:
    app.add_routes(
        [web.get('/status', lambda request: status(request, version))])
    app.add_routes([web.get('/btc', get_btc_binance_price)])
    app.add_routes([web.get('/eth', get_eth_binance_price)])
    app.add_routes([web.get('/pepe', get_pepe_binance_price)])
    app.add_routes([web.get('/pubkey', pub_ssh_key)])
    app.add_routes([web.get('/aptusdt', get_apt_binance_price)])
