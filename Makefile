dist:
	pipenv lock -r > requirements.txt

docker_build: dist
	docker build -t a1fred/mongo-cappedcollections-rest .

docker_push: docker_build
	docker push a1fred/mongo-cappedcollections-rest
