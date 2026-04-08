install:
	python -m pip install -r requirements/base.txt

run:
	uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

lint:
	python -m py_compile src/main.py
