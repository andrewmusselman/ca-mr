#!/bin/bash
input=$1
for i in {0..255}
do 
  echo $i
  ./run.sh $i $input
  echo
done
