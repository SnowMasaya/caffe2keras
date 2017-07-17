help:
	@cat Makefile

DATA?="${HOME}/Data"
DOCKER_FILE=dockerfiles/caffe_keras_ssd
DOCKER=docker
BACKEND=tensorflow
TEST=tests/
SRC=$(shell dirname `pwd`)

build:
	docker build -t keras --build-arg python_version=3.6 -f $(DOCKER_FILE) .

bash: build
	$(DOCKER) run -it -v $(SRC):/home/caffe2keras -v $(DATA):/data --env KERAS_BACKEND=$(BACKEND) keras bash

ipython: build
	$(DOCKER) run -it -v $(SRC):/home/caffe2keras -v $(DATA):/data --env KERAS_BACKEND=$(BACKEND) keras ipython

notebook: build
	$(DOCKER) run -it -v $(SRC):/home/caffe2keras -v $(DATA):/data --net=host --env KERAS_BACKEND=$(BACKEND) keras

test: build
	$(DOCKER) run -it -v $(SRC):/home/caffe2keras -v $(DATA):/data --env KERAS_BACKEND=$(BACKEND) keras py.test $(TEST)
