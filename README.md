# HTTP (DAV) based store - EXPERIMENTAL

This repository does provide a container which allows to store and retrieve
assets based on HTTP.

The implementation is based on Nginx.


## Status - EXPERIMENTAL

The container is experimental. It has been created to allow various other
containers to stay or become stateless.


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



## Example usage


### Command line using cURL

```
# Prepare a test file
echo "example content" > /tmp/example-file

# Put the file into a bucket
curl -T /tmp/example-file http://localhost:8080/example-bucket/example-file

# Retrieve the file
curl http://localhost:8080/example-bucket/example-file

# Remove the file
curl -X DELETE http://localhost:8080/example-bucket/example-file
```


## Architectural concerns

We assume that this component is only be part of interim architectures and that
an emerging target architecture would contain a service like an S3 API which can
commonly be used to hold file like assets.


## Contact

Maintained by Team SouvAP Dev.

Contact:

- johannes.bornhold.extern@univention.de
