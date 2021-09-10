FROM python:3.7

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
COPY awoo_logger-0.1.0-py3-none-any.whl /app/awoo_logger-0.1.0-py3-none-any.whl

RUN pip install -r requirements.txt
RUN pip install awoo_logger-0.1.0-py3-none-any.whl
COPY app /app

USER root

WORKDIR /

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80","--access-log"]