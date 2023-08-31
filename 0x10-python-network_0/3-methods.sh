#!/bin/bash
# script that displays the methods allowed
curl -sI "$1" | grep "Allow" | awk '{print substr($0, index($0,$2))}'
