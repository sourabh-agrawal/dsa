# Get the directory where the Makefile is located
VENV_DIR := .venv
PYTHON := python3

.PHONY: install activate deactivate clean help

install: ## Create a virtual environment in the current directory
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in: $(VENV_DIR)"

activate: ## Show command to activate the virtual environment
	@echo "Run the following command to activate the virtual environment:"
	@echo "source $(VENV_DIR)/bin/activate.fish"

deactivate: ## Show command to deactivate the virtual environment
	@echo "Run 'deactivate' in your shell to exit the virtual environment."

clean: ## Remove the virtual environment
	rm -rf $(VENV_DIR)
	@echo "Virtual environment removed from: $(VENV_DIR)"

help: ## Show available commands
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
