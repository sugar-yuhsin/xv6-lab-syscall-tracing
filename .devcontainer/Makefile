IMAGE_NAME = yunchih/nthucs-os-dev
TAG = latest
FULL_TAG = $(IMAGE_NAME):$(TAG)

.PHONY: all build tag push clean

all: build tag push

build:
	docker build -t $(IMAGE_NAME) .

tag:
	docker tag $(IMAGE_NAME) $(FULL_TAG)

push:
	docker push $(FULL_TAG)

clean:
	docker rmi $(FULL_TAG)
