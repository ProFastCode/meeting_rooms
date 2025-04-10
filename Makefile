DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
WEB_FILE = docker-compose.yml
WEB_CONTAINER = web

.PHONY: web
web:
	${DC} -f ${WEB_FILE} ${ENV} up --build -d

.PHONY: web-down
web-down:
	${DC} -f ${WEB_FILE} down

.PHONY: web-shell
web-shell:
	${EXEC} ${WEB_CONTAINER} bash

.PHONY: web-logs
web-logs:
	${LOGS} ${WEB_CONTAINER} -f

.PHONY: test
test:
	${EXEC} ${WEB_CONTAINER} python manage.py test

.PHONY: reqs
reqs:
	uv export -o requirements.txt
