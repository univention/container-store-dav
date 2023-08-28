ARG DOCKER_PROXY
ARG PYTHON_TAG=3.11

FROM ${DOCKER_PROXY}python:${PYTHON_TAG}

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install --no-cache-dir pipenv==2023.6.18 \
    && pipenv sync --system \
    && rm -r ~/.cache \
    && mkdir users \
    && mkdir conf

ENV USERLIST_FILE=/app/users/users.yaml
ENV HTPASSWD_FILE=/app/conf/htpasswd

COPY create-htpasswd.py ./

CMD [ "./create-htpasswd.py" ]
