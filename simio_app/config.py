from simio.app.config_names import AppConfig

from simio_app.mock_client import ExampleClient


def get_config():
    # fmt: off
    return {
        AppConfig: {
            AppConfig.name: "simio_app",
            AppConfig.app_path: "simio_app",
        },
        ExampleClient: {"host": "127.0.0.1"},
        'sleep_time': 5,
    }
    # fmt: on
