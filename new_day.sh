#!/bin/sh
mkdir day$1; cd day$1
touch sample;
curl -o puzzle-input -b 'session=53616c7465645f5f67b0648410072707c03e88323408112029a68cdeaf6875df04a1b4209297c3b111320bc960a15bfb' https://adventofcode.com/2021/day/$1/input
cp ../template $1.py
