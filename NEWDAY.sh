#!/bin/sh
mkdir day$1; cd day$1
touch sample;
curl -o puzzle-input -b 'session=?' https://adventofcode.com/2021/day/$1/input
cp ../template $1.py
