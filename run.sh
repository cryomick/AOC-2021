#!/bin/sh

for d in */; do echo $d; cd $d; ./*.py; cd ..; done
