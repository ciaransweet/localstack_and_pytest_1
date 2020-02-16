# LocalStack and pytest

## Prerequisites

* Python 3+

Install the required pip packages for the project with:

    $ pip3 install -r requirements.txt

## Run Localstack

The easy way is to run LocalStack with docker-compose

Run the LocalStack container in the background with:
    
    $ docker-compose up -d

Follow the logs with: 

    $ docker logs -f localstack
    
Till you see:

```
...
Waiting for all LocalStack services to be ready
Ready.
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

LocalStack is set up to invoke Lambdas in separate docker containers with `lambci`:

```
$ docker ps -a
73da88af89c3        lambci/lambda:20191117-python3.6   "/var/lang/bin/pytho…"   5 seconds ago       Exited (0) 4 seconds ago                                                focused_newton
e84c819b8dcf        localstack/localstack              "docker-entrypoint.sh"   3 minutes ago       Up 3 minutes               0.0.0.0:4567-4599->4567-4599/tcp, 8080/tcp   localstack
```

Check the container logs to see what you would in CloudWatch:
```
$ docker logs focused_newton
START RequestId: 8e231e97-8878-4bd1-b84f-eec5f1aedfc7 Version: $LATEST
[INFO]  2020-02-16T12:32:13.951Z        8e231e97-8878-4bd1-b84f-eec5f1aedfc7    I've been called!

END RequestId: 8e231e97-8878-4bd1-b84f-eec5f1aedfc7
REPORT RequestId: 8e231e97-8878-4bd1-b84f-eec5f1aedfc7 Duration: 0 ms Billed Duration: 100 ms Memory Size: 1536 MB Max Memory Used: 19 MB

{"message": "Hello pytest!"}
```

Congrats! You've run your first test against LocalStack!

To run a more complex test, repeat the above in `s3_lambda/`
