FROM python:3.8.1-slim-buster
WORKDIR /usr/src/app

COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY .. .
CMD ["flask", "run"]