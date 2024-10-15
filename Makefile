.PHONY: info deploy run_local build_local

REPO_NAME := crypto
IMAGE_NAME := price-getter
VERSION := 0.5

info: 
	@echo "REPO_NAME: $(REPO_NAME)"
	@echo "IMAGE_NAME: $(IMAGE_NAME)"
	@echo "VERSION: $(VERSION)"

deploy:
	cd deploy && \
		./deploy.yaml \
	    -e repo_name=$(REPO_NAME) \
	    -e image_name=$(IMAGE_NAME) \
	    -e tag=$(VERSION) \
	    -e build_path="/opt" \
	    -e container_name=$(IMAGE_NAME) \
	    -e container_port=8080 \
	    -e host_port=29090 \
	    -e folder_path="/opt/$(IMAGE_NAME)"

build_local:
	docker build -t $(REPO_NAME)/$(IMAGE_NAME):$(VERSION) .

run_local: build_local
	docker run -p 8080:8080 --name price-getter $(REPO_NAME)/$(IMAGE_NAME):$(VERSION)

