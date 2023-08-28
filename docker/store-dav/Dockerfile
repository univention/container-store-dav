ARG DOCKER_PROXY
FROM ${DOCKER_PROXY}library/nginx:1.23.3

RUN mkdir -p \
      /data/client_temp \
      /data/www \
    && chown -R nginx: /data

COPY entrypoint-ensure-volume-permissions.sh /docker-entrypoint.d/entrypoint-ensure-volume-permissions.sh
COPY default.conf.template /etc/nginx/templates/
