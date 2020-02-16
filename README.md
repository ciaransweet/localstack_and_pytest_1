# Localstack and pytest 1️⃣

## Prerequisites

* Python 3+

Install the required pip packages for the project with:

    $ pip3 install -r requirements.txt

## Run Localstack

The easy way is to run localstack with docker-compose

update `SERVICES` in [docker-compose.yaml](docker-compose.yaml)

Run localstack container in background.
```
$ docker-compose up -d
```

## Run tests

A simple test that creates, invokes, and then tears down a simple Lambda is provided.

To run the test, use the following commands within the root of the project:

```
$ cd lambda/basic_lambda
$ pytest -s . 
```

Wait a while, you should see similar to the following:

```
========================================================= test session starts ==========================================================
platform darwin -- Python 3.6.6, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /Users/ciaran/dev/localstack_and_pytest_1/lambda
collected 1 item                                                                                                                                                                               

test_lambda.py 
Setting up the class
.
Tearing down the class


====================================================== 1 passed in 78.43 seconds =======================================================
```

If you refer to your terminal window with Localstack running you'll also see:

```
2019-07-26T11:10:36:INFO:root: I've been called!
```

Congrats! You've run your first test against Localstack!
