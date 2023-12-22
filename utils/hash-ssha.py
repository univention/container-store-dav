#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


# Generate a SSHA hash according to RFC 2307

import base64
import hashlib
import os
import sys

password = sys.argv[1]

h = hashlib.sha1(password.encode("utf-8"))
salt = os.urandom(4)
h.update(salt)

print("{SSHA}" + base64.b64encode(h.digest() + salt).decode("utf-8"), end="")
