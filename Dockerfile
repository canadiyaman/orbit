FROM python:3.13
ENV PYTHONUNBUFFERED 1
#ENV DATABASE_URL=postgresql://orbit:orbit@db/orbit
RUN apt-get update && apt-get install

WORKDIR /orbit
COPY requirements.txt /orbit/
COPY .env-example /orbit/.env
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /orbit/

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]