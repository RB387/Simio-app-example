from typing import Optional

import trafaret as t

from simio.handler.base import BaseHandler
from simio.handler.utils import route


RequestSchema = t.Dict({
    t.Key("some_number"): t.ToInt(gte=0),
})


@route(path="/v1/hello/{user_id}/")
class ExampleHandler(BaseHandler):
    async def post(self, example: RequestSchema, user_id: int):
        return self.response({"id": user_id, "some_number": example["some_number"],})

    async def get(self, user_id: Optional[int]):
        return self.response(f"Your id is {user_id}!")
