#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = Proyecto_IngChar_MCD_SM-E
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Install Python Dependencies
.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	



## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8 and black (use `make format` to do formatting)
.PHONY: lint
lint:
	flake8 salud_mental-educacion
	isort --check --diff --profile black salud_mental-educacion
	black --check --config pyproject.toml salud_mental-educacion

## Format source code with black
.PHONY: format
format:
	black --config pyproject.toml salud_mental-educacion






#################################################################################
# PROJECT RULES                                                                 #
#################################################################################


## Make Dataset
.PHONY: data
data: requirements
	$(PYTHON_INTERPRETER) salud_mental-educacion/dataset.py


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
