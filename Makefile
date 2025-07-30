ENV_DIR=env
BACKEND_DIR=backend
PYTHON=$(ENV_DIR)/bin/python
PIP=$(ENV_DIR)/bin/pip
FRONTEND_DIR=frontend

.DEFAULT_GOAL := help

help:
	@echo "Usage:"
	@echo "  make setup           - Setup backend virtualenv and install Python deps"
	@echo "  make run             - Run backend FastAPI app"
	@echo "  make frontend-run    - Run frontend dev server"
	@echo "  make dev             - Run both backend and frontend dev servers concurrently"
	@echo "  make clean           - Remove backend virtualenv"
	@echo "  make freeze          - Freeze backend dependencies to requirements.txt"

setup:
	cd $(BACKEND_DIR) && python3 -m venv $(ENV_DIR)
	cd $(BACKEND_DIR) && source env/bin/activate
	cd $(BACKEND_DIR) && $(PIP) install --upgrade pip
	cd $(BACKEND_DIR) && $(PIP) install -r requirements.txt

backend-run:
	cd $(BACKEND_DIR) && $(PYTHON) -m uvicorn main:app --reload

frontend-run:
	cd $(FRONTEND_DIR) && npm install
	cd $(FRONTEND_DIR) && npm run dev

dev:
	# Run frontend and backend concurrently
	$(MAKE) frontend-run & $(MAKE) backend-run

clean:
	rm -rf $(BACKEND_DIR)/$(ENV_DIR)

freeze:
	cd $(BACKEND_DIR) && $(PIP) freeze > requirements.txt
