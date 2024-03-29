# DEPRECATED

The repository you are looking into is now deprecated in favor of object storage.

It contains proof of concept and preview builds in development created in
context of the [openDesk](https://gitlab.opencode.de/bmi/souveraener_arbeitsplatz/info) project.

The repository's content provides you with first insights into the containerized cloud IAM from Univention, derived from the UCS appliance.

## Status - DEPRECATED

The container is deprecated. It was been created to allow various other
containers to stay or become stateless.


# HTTP (DAV) based store - DEPRECATED

This repository does provide a container which allows to store and retrieve
assets based on HTTP.

The implementation is based on Nginx.


## Usage idea

We've seen a pattern where services share data based on the filesystem around
the containerization of various UCS components.

For the containerization this is a pattern which has some drawbacks involved, we
would basically glue many containers together so that they could share volumes
or similar aspects.

A common pattern in the container world would be to use a service which does
provide an S3 like API, so that assets could be stored via a well established
API.

When doing the initial containerization we found that the simplest possible
pattern which does keep the design attributes of an S3 like service would be to
use a HTTP server which does allow `PUT` and `DELETE` calls to manage assets.

A quick research did lead us to find that a subset of WebDAV would likely be
sufficient. In particular Nginx does provide a corresponding module and is our
first candidate of choice.



## Usage

### `docker-compose` based local dev environment

Use the same project name to ensure that the `portal-server` can reach the
`store-dav`.

Either by specifying the project name on the command line:

```
docker compose -p portal-dev up
```

Or by setting the toplevel attribute `name` in your
`docker-compose.override.yaml`:

```yaml
version: "3.9"
name: portal-dev
services:
# [...]
```

## Example usage


### Command line using cURL

```sh
# Prepare a test file
echo "example content" > /tmp/example-file

# Put the file into a bucket
curl -T /tmp/example-file http://localhost:8080/example-bucket/example-file

# Retrieve the file
curl http://localhost:8080/example-bucket/example-file

# Remove the file
curl -X DELETE http://localhost:8080/example-bucket/example-file
```


### Test usage with the portal server

```sh
# Fetch data from UCS machine
curl --user portal-server:univention http://localhost/univention/internal/portal > /tmp/portal
curl --user portal-server:univention http://localhost/univention/internal/groups > /tmp/groups

# Put the data into a bucket "portal-data"
curl -T /tmp/portal http://localhost:8081/portal-data/portal
curl -T /tmp/groups http://localhost:8081/portal-data/groups

# Verify that the data is there
curl http://localhost:8081/portal-data/
curl http://localhost:8081/portal-data/portal
curl http://localhost:8081/portal-data/groups
```

Adjust configuration of the `portal-server`, e.g. in your file
`docker-compose.override.yaml`:

```yaml
services:
  portal-server:
    environment:
      # PORTAL_SERVER_UCS_INTERNAL_URL: "http://host.docker.internal:8000/univention/internal"
      PORTAL_SERVER_UCS_INTERNAL_URL: "http://store-dav/portal"
```

After bringing everything up and using the same docker compose project name,
test that the `portal-server` can reach `store-dav`:

```sh
docker compose exec -it portal-server /bin/bash
curl store-dav
```


## Architectural concerns

We assume that this component is only be part of interim architectures and that
an emerging target architecture would contain a service like an S3 API which can
commonly be used to hold file like assets.


## Contact

Maintained by Team SouvAP Dev.
