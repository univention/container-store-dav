#!/bin/bash
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH

set -euxo pipefail

state_dir="/data"
current_owner="$(stat -c "%U" "${state_dir}")"

if [ "${current_owner}" != "nginx" ]
then
    echo "Trying to adjust owner of directory ${state_dir}"
    chown -R nginx: "${state_dir}"
fi
