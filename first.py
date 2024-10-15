from src.routes import setup_routes
from aiohttp import web
import os

VERSION = os.getenv('APP_VERSION', '1.0.0')


def main():
    app = web.Application()
    setup_routes(app, VERSION)
    web.run_app(app)


if __name__ == '__main__':
    main()
