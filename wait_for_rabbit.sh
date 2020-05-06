#!/bin/bash
set -e

until timeout 1 bash -c "cat < /dev/null > /dev/tcp/rabbitmq/5672"; do
  >&2 echo "Rabbit MQ not up yet on rabbit"
  sleep 1
done

echo "Rabbit MQ is up"
