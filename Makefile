all: build

build:
	docker-compose build
	docker-compose up -d

run:
	docker-compose up -d
