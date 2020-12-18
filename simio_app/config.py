import os
from pathlib import Path

from simio.app.config_names import APP, CLIENTS, VARS, DIRECTORS
from simio.app import AsyncCronsDirector, AsyncWorkersDirector

from simio_app.crons.heartbeat import heartbeat
from simio_app.workers.ping import ping_worker
from simio_app.mock_client import ExampleClient


def get_config():
    # fmt: off
    return {
        APP: {
            APP.name: "simio_app",
            APP.handlers_path: Path(__file__).parent / "handlers",
        },
        CLIENTS: {
            ExampleClient: {
                "host": "localhost",
                "port": 27017,
            },
        },
        VARS: {
            "x": os.getenv("X"),
            "y": os.getenv("Y"),
        },
        DIRECTORS: {
            AsyncWorkersDirector: {
                ping_worker: {
                    "sleep_time": 5
                },
            },
            AsyncCronsDirector: {
                "*/1 * * * *": (
                    heartbeat,
                ),
            },
        },
    }
    # fmt: on
