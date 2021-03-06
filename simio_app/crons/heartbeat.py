from datetime import datetime

from simio import web
from simio.job import async_cron
from simio_di import Depends

from simio_app.mock_client import ExampleClient


@async_cron.register(cron="*/1 * * * *")
async def heartbeat(app: web.Application, client: Depends[ExampleClient]):

    heartbeat_document = {
        "timestamp": datetime.now().timestamp(),
        "message": "still alive",
    }
    app.logger.info(heartbeat_document)

    client.db.collection.insert(heartbeat_document)