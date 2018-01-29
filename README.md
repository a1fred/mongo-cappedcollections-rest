# Dead simple mongodb capped collections rest api
Simple mongodb rest wrapper for write data to capped collections

# REST api
GET / - collections index
GET /<collection_name> - show entities
POST /collection_name - create

# Docker usage
enviroement variables:
* MONGODB_CONNECTION_STRING
* MONGODB_DB_NAME

Run container
```shell
docker run -e "MONGODB_CONNECTION_STRING=mongodb://localhost:27017" -e "MONGODB_DB_NAME=mongorest" -p 5000 a1fred/mongorest
```

```yml
    version: '3'

    services:
        mongodb:
            restart: always
            image: mongo:3.7
            volumes:
            - /data/db
            ports:
            - "27017:27017"
        mongorest:
            restart: always
            image: a1fred/mongo-cappedcollections-rest
            depends_on:
            - mongodb
            environment:
            MONGODB_CONNECTION_STRING: mongodb://mongodb:27017
            ports:
            - "127.0.0.1:5000:5000"
```
