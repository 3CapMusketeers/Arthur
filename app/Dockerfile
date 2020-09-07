FROM python:3.8.1-slim-buster
WORKDIR /usr/src/app

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV BASE_URL=https://api.spotify.com
ENV AUTH_URL=https://accounts.spotify.com/authorize
ENV API_TOKEN_URL=https://accounts.spotify.com/api/token

ENV CLIENT_ID=369a6c4b828e4dda98c6a47e891d5b2f
ENV REDIRECT_URI=http://localhost:5000/authentication
ENV CLIENT_SECRET=5be944b9cb9b4897849438c3f586f9e5

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]