# Localstack and pytest 1️⃣

## Prerequisites

* Python (I'm using 3.6.6)
* Pycharm/some IDE

Install the required pip packages for the project with:

`$ pip3 install -r requirements.txt`

## How to run Localstack

When run as a service, Localstack sometimes has issues with where it puts its temporary folders,
I like to create a directory locally which I know it will be OK with. Run the following in the root of
the project:

`$ mkdir localstacktmp`

To run only the services you require for 'basic' Lambda development, Localstack provides a shorthand 
option to minimise what you spin up.

`$ env SERVICES=serverless TMPDIR=./localstacktmp localstack start`

You should see the following after a few seconds:

```
$ env SERVICES=serverless TMPDIR=./localstacktmp localstack start
Starting local dev environment. CTRL-C to quit.
Starting mock S3 (http port 4572)...
Starting mock SNS (http port 4575)...
Starting mock IAM (http port 4593)...
Starting mock API Gateway (http port 4567)...
Starting mock DynamoDB (http port 4569)...
Starting mock Lambda service (http port 4574)...
Starting mock CloudWatch Logs (http port 4586)...
Ready.
```

## How to run tests

A simple test that creates, invokes, and then tears down a simple Lambda is provided.

As your terminal will be taken up by the Localstack service running, either open a new terminal window or 
create a new pane in your favourite multiplexer of choice!

To run the test, use the following commands within the root of the project:

```
$ cd lambda
$ pytest -s . 
```

You should see similar to the following:

```
== test session starts ==
platform darwin -- Python 3.6.6, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /Users/ciaran/dev/localstack_and_pytest_1/lambda
collected 1 item                                                                                                                                                                               

test_lambda.py 
Setting up the class
.
Tearing down the class


== 1 passed in 0.29 seconds ==
```

If you refer to your terminal window with Localstack running you'll also see:

`2019-07-26T11:10:36:INFO:root: I've been called!`

Congrats! You've run your first test against Localstack!
