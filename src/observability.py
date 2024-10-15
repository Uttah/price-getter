from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def status(request: Request, version: str) -> Response:
    return web.json_response({
        'status': 'ok',
        'version': version
    })
