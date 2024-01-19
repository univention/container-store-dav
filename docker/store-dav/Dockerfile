# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH

FROM gitregistry.knut.univention.de/univention/customers/dataport/upx/container-nginx/nginx:0.1.1

RUN mkdir -p \
      /data/client_temp \
      /data/www \
    && chown -R nginx: /data

COPY nginx.conf /etc/nginx/nginx.conf
