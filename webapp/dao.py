from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import Collection


def get_client(connection_string: str, database_name: str) -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(connection_string)['database_name']
    return client


async def get_collection(client: AsyncIOMotorClient, collection: str, size=10000) -> Collection:
    collection_names = await client.collection_names()
    if collection not in collection_names:
        return await client.create_collection(collection, capped=True, size=size)
    else:
        return client[collection]
