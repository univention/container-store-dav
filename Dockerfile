ARG DOCKER_PROXY
FROM ${DOCKER_PROXY}library/nginx:1.23.3

RUN mkdir -p \
      /data/client_temp \
      /data/www \
    && chown -R nginx: /data

COPY default.conf.template /etc/nginx/templates/
