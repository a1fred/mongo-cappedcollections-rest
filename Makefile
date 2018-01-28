dist:
	pipenv lock -r > requirements.txt

docker_build: dist
	docker build -t mongorest .
