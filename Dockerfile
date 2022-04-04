# syntax=docker/dockerfile:1

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-bullseye

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ADD . /
WORKDIR /

RUN python -m pip install -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=development

ENV LISTEN_PORT=5000
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["app.py"]

