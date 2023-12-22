#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


"""
Generates a `htpasswd` file with `SSHA` hashes.

This script consumes an input file `users.yaml` which contains a map from
`<username>` to `<password>`. It generates a new file `htpasswd` based on this
data, in `htpasswd` all passwords will be hashed via `SSHA`.

The following environment variables can be set to configure this script:

- `USERLIST_FILE` to define where to find the user list.

- `HTPASSWD_FILE` to define where to write the `htpasswd` output.
"""

import base64
import hashlib
import logging
import os

import yaml


log = logging.getLogger("create-htpasswd")


def main():
    logging.basicConfig(level=logging.INFO)
    config = get_config_from_env()
    users = load_users(config["users_file"])
    hash_passwords(users)
    write_htpasswd(users, config["htpasswd_file"])
    log.info("htpasswd file created: %s", config["htpasswd_file"])


def get_config_from_env():
    users_file = os.environ["USERLIST_FILE"]
    htpasswd_file = os.environ["HTPASSWD_FILE"]
    config = {
        "users_file": users_file,
        "htpasswd_file": htpasswd_file,
    }
    log.info("Configuration: %s", config)
    return config


def load_users(filename):
    log.debug("Loading users from %s", filename)
    users = yaml.safe_load(open(filename, "r"))
    log.info("Users list: %s", list(users.keys()))
    return users


def hash_passwords(users):
    for username, password in users.items():
        users[username] = generate_ssha_hash(password)


def generate_ssha_hash(password, salt=None):
    """Generate a SSHA hash according to RFC 2307"""
    h = hashlib.sha1(password.encode("utf-8"))
    salt = os.urandom(4)
    h.update(salt)
    return "{SSHA}" + base64.b64encode(h.digest() + salt).decode("utf-8")


def write_htpasswd(users, filename):
    lines = []
    for username, password_or_hash in users.items():
        lines.append(f"{username}:{password_or_hash}")
    content = "\n".join(lines)
    with open(filename, "w") as htpasswd_file:
        htpasswd_file.write(content)


if __name__ == "__main__":
    main()
