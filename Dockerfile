FROM python:3

MAINTAINER Ayman E
LABEL version="1.0.0"
LABEL maintaner="Ayman E"
LABEL release-date="2025-Dec-12"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]