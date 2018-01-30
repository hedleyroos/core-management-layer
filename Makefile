VENV=./ve
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
FLAKE8=$(VENV)/bin/flake8
PYTEST=$(VENV)/bin/pytest
FLASK=$(VENV)/bin/flask
CODEGEN_VERSION=2.3.1
CODEGEN=java -jar swagger-codegen-cli-$(CODEGEN_VERSION).jar generate
USER_DATA_STORE_CLIENT_DIR=management_layer/user_data_store
ACCESS_CONTROL_CLIENT_DIR=management_layer/access_control
AUTHENTICATION_SERVICE_CLIENT_DIR=management_layer/authentication_service

# Colours.
CLEAR=\033[0m
RED=\033[0;31m
GREEN=\033[0;32m
CYAN=\033[0;36m

.SILENT: docs-build
.PHONY: check test

help:
	@echo "usage: make <target>"
	@echo "    $(CYAN)build-virtualenv$(CLEAR): Creates virtualenv directory, 've/', in project root."
	@echo "    $(CYAN)clean-virtualenv$(CLEAR): Deletes 've/' directory in project root."
	@echo "    $(CYAN)docs-build$(CLEAR): Build documents and place html output in docs root."

$(VENV):
	@echo "$(CYAN)Initialise base ve...$(CLEAR)"
	virtualenv $(VENV) -p python3
	@echo "$(GREEN)DONE$(CLEAR)"

# Creates the virtual environment.
build-virtualenv: $(VENV)
	@echo "$(CYAN)Building virtualenv...$(CLEAR)"
	# TODO: Depending on project type, requirements will need to be installed here.
	@echo "$(GREEN)DONE$(CLEAR)"

# Deletes the virtual environment.
clean-virtualenv:
	@echo "$(CYAN)Clearing virtualenv...$(CLEAR)"
	rm -rf $(VENV)
	@echo "$(GREEN)DONE$(CLEAR)"

# Build sphinx docs, then move them to docs/ root for GitHub Pages usage.
docs-build:  $(VENV)
	@echo "$(CYAN)Installing Sphinx requirements...$(CLEAR)"
	$(PIP) install sphinx sphinx-autobuild
	@echo "$(GREEN)DONE$(CLEAR)"
	@echo "$(CYAN)Backing up docs/ directory content...$(CLEAR)"
	tar -cvf backup.tar docs/source docs/Makefile
	@echo "$(GREEN)DONE$(CLEAR)"
	@echo "$(CYAN)Clearing out docs/ directory content...$(CLEAR)"
	rm -rf docs/
	@echo "$(GREEN)DONE$(CLEAR)"
	@echo "$(CYAN)Restoring base docs/ directory content...$(CLEAR)"
	tar -xvf backup.tar
	@echo "$(GREEN)DONE$(CLEAR)"
	# Remove the tar file.
	rm backup.tar
	# Actually make html from index.rst
	@echo "$(CYAN)Running sphinx command...$(CLEAR)"
	$(MAKE) -C docs/ clean html SPHINXBUILD=../$(VENV)/bin/sphinx-build
	@echo "$(GREEN)DONE$(CLEAR)"
	@echo "$(CYAN)Moving build files to docs/ root...$(CLEAR)"
	cp -r docs/build/html/. docs/
	rm -rf docs/build/
	@echo "$(GREEN)DONE$(CLEAR)"

swagger-codegen-cli-$(CODEGEN_VERSION).jar:
	wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/$(CODEGEN_VERSION)/swagger-codegen-cli-$(CODEGEN_VERSION).jar

prism:
	curl -L https://github.com/stoplightio/prism/releases/download/v0.6.21/prism_linux_amd64 -o prism
	chmod +x prism

mock-management-layer-api: prism
	./prism run --mockDynamic --list -s swagger/management_layer.yml -p 8010

validate-swagger: prism
	@./prism validate -s swagger/management_layer.yml && echo "The Swagger spec contains no errors"

$(FLAKE8): $(VENV)
	$(PIP) install flake8

# Generate the client code to interface with the User Data Store
user-data-store-client: swagger-codegen-cli-$(CODEGEN_VERSION).jar
	echo "Generating the client for the User Data Store API..."
	# curl https://github.com/girleffect/core-user-data-store/blob/develop/swagger/user_data_store.yml -o user_data_store.yml
	#$(CODEGEN) -l python -i user_data_store.yml -o $(USER_DATA_STORE_CLIENT_DIR)
	$(CODEGEN) -l python -i ../core-user-data-store/swagger/user_data_store.yml -o /tmp/$(USER_DATA_STORE_CLIENT_DIR)
	cp -r /tmp/$(USER_DATA_STORE_CLIENT_DIR)/swagger_client* $(USER_DATA_STORE_CLIENT_DIR)

# Generate the client code to interface with the Access Control component
access-control-client: swagger-codegen-cli-$(CODEGEN_VERSION).jar
	echo "Generating the client for the Access Control API..."
	# curl https://github.com/girleffect/core-access-control/blob/develop/swagger/access_control.yml -o access_control.yml
	#$(CODEGEN) -l python -i access_control.yml -o /tmp/$(ACCESS_CONTROL_CLIENT_DIR)
	$(CODEGEN) -l python -i ../core-access-control/swagger/access_control.yml -o /tmp/$(ACCESS_CONTROL_CLIENT_DIR)
	cp -r /tmp/$(ACCESS_CONTROL_CLIENT_DIR)/swagger_client* $(ACCESS_CONTROL_CLIENT_DIR)

# Generate the client code to interface with the Authentication Service
authentication-service-client: swagger-codegen-cli-$(CODEGEN_VERSION).jar
	echo "Generating the client for the Authentication Service API..."
	# curl https://github.com/girleffect/core-authentication-service/blob/develop/swagger/authentication_service.yml -o authentication_service.yml
	#$(CODEGEN) -l python -i authentication_service.yml -o $(AUTHENTICATION_SERVICE_CLIENT_DIR)
	$(CODEGEN) -l python -i ../core-authentication-service/swagger/authentication_service.yml -o /tmp/$(AUTHENTICATION_SERVICE_CLIENT_DIR)
	cp -r /tmp/$(AUTHENTICATION_SERVICE_CLIENT_DIR)/swagger_client* $(AUTHENTICATION_SERVICE_CLIENT_DIR)

management-layer-api: swagger-codegen-cli-$(CODEGEN_VERSION).jar validate-swagger
	$(CODEGEN) -i swagger/management_layer.yml -l python-flask -o .

runserver: $(VENV)
	@echo "$(CYAN)Firing up server...$(CLEAR)"
	$(PYTHON) -m swagger_server

check: $(FLAKE8)
	$(FLAKE8)

$(PYTEST): $(VENV)
	$(PIP) install pytest pytest-cov

test: $(PYTEST)
	$(PYTEST) --verbose --cov=management_layer --cov=swagger_server/controllers/ management_layer/
