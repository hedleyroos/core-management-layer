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
curl -d grant_type=password -d username=admin -d password=local -d client_id=client_id_1 -d client_secret=super_client_secret_1 -d scope=openid%20profile%20email%20address%20phone%20site%20roles -X POST "http://172.18.0.3:8000/openid/token/"
```
The response will look like this:
```json
{
    "access_token": "a229b25953874582849298c69ec9d7f8",
    "expires_in": 3600,
    "id_token": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTcyLjE4LjAuMzo4MDAwL29wZW5pZCIsInN1YiI6ImJjMzZiNDM2LTEwOTEtMTFlOC1iYzBmLTAyNDJhYzEyMDAwMyIsImF1ZCI6ImNsaWVudF9pZF8xIiwiZXhwIjoxNTE5ODQyMzkzLCJpYXQiOjE1MTk4NDE3OTMsImF1dGhfdGltZSI6MTUxOTgxNTM2Nywibm9uY2UiOiJzZWxmLmNvZGUubm9uY2UiLCJhdF9oYXNoIjoiS1VxUTV1UTFhWncxcjRHeTZQblNmdyJ9.D-_Ww_dwF1uXHw-Vpfa808S3s46386D5FACLfczfqPs",
    "refresh_token": "3f3f53de8f1f49d9851902aca0f9add8",
    "token_type": "bearer"
}
```
Copy the `id_token` and use it with the API Key Authentication method of
the Swagger UI. The value of the field must be `bearer <id_token>`.





