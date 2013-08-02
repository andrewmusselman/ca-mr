#!/bin/bash
rule=$1
input=`cat $2`
for i in {1..40}
do
  echo $input
  input=`echo $input | ./m.py $rule`
done
