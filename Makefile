VENV=./ve
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
FLAKE8=$(VENV)/bin/flake8
PYTEST=$(VENV)/bin/pytest
FLASK=$(VENV)/bin/flask
CODEGEN_VERSION=2.4.0
CODEGEN=java -jar swagger-codegen-cli-$(CODEGEN_VERSION).jar generate
USER_DATA_STORE_CLIENT_DIR=user_data_store
ACCESS_CONTROL_CLIENT_DIR=access_control
AUTHENTICATION_SERVICE_CLIENT_DIR=authentication_service

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
	# curl https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/$(CODEGEN_VERSION)/swagger-codegen-cli-$(CODEGEN_VERSION).jar
	# We use the development snapshot until the 2.4.0 release is actually made.
	# The previous version (2.3.1) contains bugs which have been fixed, but not released.
	# Once 2.4.0 is officially released, we can download the non-SNAPSHOT version.
	curl https://oss.sonatype.org/content/repositories/snapshots/io/swagger/swagger-codegen-cli/$(CODEGEN_VERSION)-SNAPSHOT/swagger-codegen-cli-$(CODEGEN_VERSION)-20180411.010038-223.jar -o swagger-codegen-cli-$(CODEGEN_VERSION).jar

prism:
	curl -L https://github.com/stoplightio/prism/releases/download/v0.6.21/prism_linux_amd64 -o prism
	chmod +x prism

mock-management-layer-api: prism
	./prism run --cors --mockDynamic --list -s swagger/management_layer.yml -p 8010

validate-swagger: prism
	@./prism validate -s swagger/management_layer.yml && echo "The Swagger spec contains no errors"

$(FLAKE8): $(VENV)
	$(PIP) install flake8

swagger/user_data_store.yml:
	curl https://raw.githubusercontent.com/girleffect/core-user-data-store/develop/swagger/user_data_store.yml -o swagger/user_data_store.yml

swagger/access_control.yml:
	curl https://raw.githubusercontent.com/girleffect/core-access-control/develop/swagger/access_control.yml -o swagger/access_control.yml

swagger/authentication_service.yml:
	curl https://raw.githubusercontent.com/girleffect/core-authentication-service/develop/swagger/authentication_service.yml -o swagger/authentication_service.yml

# Generate the client code to interface with the User Data Store
user-data-store-client: swagger-codegen-cli-$(CODEGEN_VERSION).jar swagger/user_data_store.yml
	echo "Generating the client for the User Data Store API..."
	$(CODEGEN) --lang python --library asyncio -i swagger/user_data_store.yml -D packageName=user_data_store -o /tmp/$(USER_DATA_STORE_CLIENT_DIR)
	cp -r /tmp/$(USER_DATA_STORE_CLIENT_DIR)/user_data_store/* $(USER_DATA_STORE_CLIENT_DIR)

# Generate the client code to interface with the Access Control component
access-control-client: swagger-codegen-cli-$(CODEGEN_VERSION).jar swagger/access_control.yml
	echo "Generating the client for the Access Control API..."
	$(CODEGEN) --lang python --library asyncio -i swagger/access_control.yml -D packageName=access_control -o /tmp/$(ACCESS_CONTROL_CLIENT_DIR)
	cp -r /tmp/$(ACCESS_CONTROL_CLIENT_DIR)/access_control/* $(ACCESS_CONTROL_CLIENT_DIR)

# Generate the client code to interface with the Authentication Service
authentication-service-client: swagger-codegen-cli-$(CODEGEN_VERSION).jar swagger/authentication_service.yml
	echo "Generating the client for the Authentication Service API..."
	$(CODEGEN) --lang python --library asyncio -i swagger/authentication_service.yml -D packageName=authentication_service -o /tmp/$(AUTHENTICATION_SERVICE_CLIENT_DIR)
	cp -r /tmp/$(AUTHENTICATION_SERVICE_CLIENT_DIR)/authentication_service/* $(AUTHENTICATION_SERVICE_CLIENT_DIR)

management-layer-api: validate-swagger
	$(PYTHON) $(VENV)/src/swagger-django-generator/swagger_django_generator/generator.py swagger/management_layer.yml --output-dir management_layer/api --module-name management_layer.api --backend aiohttp

runserver: $(VENV)
	@echo "$(CYAN)Firing up server...$(CLEAR)"
	STUBS_CLASS=management_layer.integration.Implementation PYTHONASYNCIODEBUG=1 $(PYTHON) httpd.py

check: $(FLAKE8)
	$(FLAKE8)

$(PYTEST): $(VENV)
	$(PIP) install pytest pytest-cov

test: $(PYTEST)
	$(PYTEST) --verbose --cov=management_layer management_layer/ --log-level=DEBUG
