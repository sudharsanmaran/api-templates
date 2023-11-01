FROM python:3.11.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip && pip3 install --upgrade setuptools

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--port=8003", "--reload", "--forwarded-allow-ips=*"]