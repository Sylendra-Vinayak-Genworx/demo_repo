FROM python:3.12-slim

WORKDIR /app

RUN python -m pip install --upgrade pip
COPY requirements/base.txt ./requirements/base.txt
RUN pip install -r requirements/base.txt

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
