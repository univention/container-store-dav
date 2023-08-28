# Config htpasswd

This is a small utility container to help assemble the `htpasswd` file for the
password protection of `store-dav`.

The idea is that this container will as input receive the list of desired
usernames and passwords. With this it will generate the `htpasswd` file in a
structure which is suitable for Nginx to consume.


## Local testing

The container is basically a simple Python script. Local testing can be done
either by the `docker` CLI or by using `pipenv` to quickly set up a Python
virtual environment:

```shell
# Python virtual environment
pipenv sync
pipenv shell

# Docker CLI
docker build . -t wip
docker run wip bash
```
