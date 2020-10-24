from aiohttp import web
from simio.app.builder import AppBuilder
from simio_app.config import get_config


def main():
    config = get_config()
    builder = AppBuilder(config)
    app = builder.build_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
