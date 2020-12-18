import logging

from simio.app import AppBuilder

from simio_app.config import get_config

logging.basicConfig(level=logging.INFO)


def main():
    builder = AppBuilder(get_config())
    app = builder.build_app()
    app.run()


if __name__ == "__main__":
    main()
