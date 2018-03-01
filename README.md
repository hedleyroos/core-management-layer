# Management Layer
[![Build Status](https://travis-ci.org/girleffect/core-management-layer.svg?branch=develop)](https://travis-ci.org/girleffect/core-management-layer)
[![Coverage Status](https://coveralls.io/repos/github/girleffect/core-management-layer/badge.svg?branch=cobusc-coverage)](https://coveralls.io/github/girleffect/core-management-layer?branch=cobusc-coverage)

## Overview
TODO

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 httpd.py
```
or use the shortcut `make run`

and open your browser to see the Swagger UI here:

```
http://localhost:8000/ui/index.html
```

Your Swagger definition lives here:

```
http://localhost:8000/the_specification
```

To launch the integration tests, run:
```
make test
```

## Demo Environment

### Swagger UI

To obtain a key that be used to demonstrate the API functionality via
the Swagger UI, do the following:

```
curl -d grant_type=password -d username=admin -d password=local -d client_id=management_layer_workaround -d client_secret=management_layer_workaround -d scope=openid%20profile%20email%20address%20phone%20site%20roles -X POST "http://172.18.0.3:8000/openid/token/" --proxy "http://localhost:3128" | python -m json.tool
```
The response will look like this:
```json
{
    "access_token": "875d64bae0284ab9849badb7d419acf1",
    "expires_in": 3600,
    "id_token": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTcyLjE4LjAuMzo4MDAwL29wZW5pZCIsInN1YiI6ImJjMzZiNDM2LTEwOTEtMTFlOC1iYzBmLTAyNDJhYzEyMDAwMyIsImF1ZCI6Im1hbmFnZW1lbnRfbGF5ZXJfd29ya2Fyb3VuZCIsImV4cCI6MTUxOTg5MzIzNiwiaWF0IjoxNTE5ODkyNjM2LCJhdXRoX3RpbWUiOjE1MTk4NDY5MTAsIm5vbmNlIjoic2VsZi5jb2RlLm5vbmNlIiwiYXRfaGFzaCI6IlFCVzBvMUZUb196TXpyTWM3YWY5NHcifQ.keXF-fXtRosaU-C9GKE60JPYERTjR_l6f9EEHppolys",
    "refresh_token": "e2c0c5458a2b4ea4bed5ffca4c825af8",
    "token_type": "bearer"
}
```
Copy the `id_token` and use it with the API Key Authentication method of
the Swagger UI. The value of the field must be `bearer <id_token>`.

### Checking identity tokens

Paste the token into form provided by [https://jwt.io](jwt.io).

### Checking timestamps

The `exp`, `iat` and `issued_at` fields are seconds since the Epoch.
To quickly convert to a human readable datetime, use the following bash
command :
```
printf "%(%F %T)T" 1519893236
2018-03-01 10:33:56
```


