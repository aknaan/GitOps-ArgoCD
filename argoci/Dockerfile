FROM python:3.12-slim AS build
WORKDIR /project
COPY /project /project
RUN pip install -r requirements.txt --break-system-packages
CMD gunicorn --bind 0.0.0.0:80 -m 000 python_project:app


