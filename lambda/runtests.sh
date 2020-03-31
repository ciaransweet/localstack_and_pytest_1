#!/usr/bin/env bash

echo "Waiting for LocalStack to launch..."

while ! nc -z localstack 4567; do
  sleep 1
done

while ! nc -z localstack 4574; do
  sleep 1
done

echo -e "\tLocalStack launched\n"

echo -e "Testing basic_lambda\n\n"
cd basic_lambda
pytest -s .
echo

echo -e "Testing s3_lambda\n\n"
cd ../s3_lambda
pytest -s .
echo
