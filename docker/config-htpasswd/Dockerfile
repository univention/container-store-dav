# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH

ARG UCS_BASE_IMAGE=gitregistry.knut.univention.de/univention/components/ucs-base-image/ucs-base-520
ARG UCS_BASE_IMAGE_TAG=0.11.2

FROM ${UCS_BASE_IMAGE}:${UCS_BASE_IMAGE_TAG} AS build-base

WORKDIR /app

RUN apt-get update -qq && \
    apt-get install --assume-yes --verbose-versions --no-install-recommends \
      python3-minimal=3.11.* \
      python3-pip=23.0.* && \
    rm -fr /var/lib/apt/lists/* /var/cache/apt/archives/* && \
    rm /usr/lib/python3.11/EXTERNALLY-MANAGED

COPY Pipfile Pipfile.lock ./

RUN pip3 install --no-cache-dir pipenv==2023.6.18 \
    && pipenv sync --system \
    && apt-get purge -y python3-pip \
    && rm -r ~/.cache \
    && mkdir users \
    && mkdir conf

ENV USERLIST_FILE=/app/users/users.yaml
ENV HTPASSWD_FILE=/app/conf/htpasswd

COPY create-htpasswd.py ./

CMD [ "./create-htpasswd.py" ]
