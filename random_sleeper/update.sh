#!/bin/sh

sam build --debug --cached --use-container --cached

if [ "$?" -eq "0" ]
then
  sam deploy --no-fail-on-empty-changeset --no-confirm-changeset
else
  echo "build failed!"
fi

echo "finished at $(date)"