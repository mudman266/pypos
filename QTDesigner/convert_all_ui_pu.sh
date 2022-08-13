#!/usr/bin/env bash

for file in ./*.ui; do
  pyuic6 -o ../src/${file:2:-2}py ${file:2}
done
echo 'done'
