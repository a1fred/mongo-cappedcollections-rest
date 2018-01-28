import os

from sanic.views import HTTPMethodView
from sanic.request import Request
from motor.core import Collection

from webapp import dao


class CoreView(HTTPMethodView):
    request: Request
    collection_name: str
    mongo_connection_string = os.getenv('MONGODB_CONNECTION_STRING', 'mongodb://localhost:27017')
    mongo_db_name = os.getenv('MONGODB_DB_NAME', 'mongorest')

    def get_client(self):
        return dao.get_client(self.mongo_connection_string, self.mongo_db_name)

    async def get_collection(self) -> Collection:
        client = self.get_client()
        size = self.request.args.get('size', 10000)
        return await dao.get_collection(client, self.collection_name, size=size)

    def dispatch_request(self, request, **kwargs):
        handler = getattr(self, request.method.lower(), None)
        self.request = request
        return handler(**kwargs)


class CollectionCoreView(CoreView):
    def dispatch_request(self, request, collection_name, **kwargs):
        handler = getattr(self, request.method.lower(), None)
        self.request = request
        self.collection_name = collection_name
        return handler(**kwargs)
