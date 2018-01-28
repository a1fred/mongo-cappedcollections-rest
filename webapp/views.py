from sanic.response import json
from sanic.request import Request
from sanic.response import json
from bson.objectid import ObjectId
from datetime import datetime

from .core.views import CoreView, CollectionCoreView


class CollectionsIndexView(CoreView):
    async def get(self):
        client = self.get_client()

        return json({
            'collections': await client.collection_names(),
        })


class CollectionView(CollectionCoreView):
    async def get(self):
        collection = await self.get_collection()

        items = await collection.find({}).sort('datetime', -1).to_list(length=100)
        for document in items:
            document['_id'] = str(document['_id'])

        return json({
            'items': items,
        })

    async def post(self):
        collection = await self.get_collection()

        data = self.request.json
        if '_id' in data:
            del data['_id']
        data['datetime'] = datetime.utcnow()

        result = await collection.insert_one(data)
        document = await collection.find_one({
            "_id": ObjectId(result.inserted_id),
        })
        document['_id'] = str(document['_id'])

        return json({
            "document": document,
        })
