FROM python:3.10-alpine

ENV APP_DIR="/opt/gitlab"
ENV PYTHONPATH="${APP_DIR}/gitlab_api"
ARG PYTHONPATH="${PYTHONPATH}"
WORKDIR ${APP_DIR}
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "main.py" ]