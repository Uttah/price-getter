FROM python:3.10.8-slim

ADD . /app
RUN pip install \
  aiohttp \
  requests

WORKDIR /app

EXPOSE 8080
CMD [ "python", "first.py" ]
