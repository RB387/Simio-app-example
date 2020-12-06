from datetime import datetime

from aiohttp import web

from simio.app.config_names import CLIENTS

from simio_app.mock_client import ExampleClient


async def heartbeat(app: web.Application):
    db_client = app[CLIENTS][ExampleClient]

    heartbeat_document = {
        "timestamp": datetime.now().timestamp(),
        "message": "still alive",
    }
    app.logger.info(heartbeat_document)

    db_client.db.collection.insert(heartbeat_document)
