FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /scraping_server

WORKDIR /scraping_server

ADD . /scraping_server/

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn"]

CMD ["--reload", "-b", "0.0.0.0", "server:api"]
