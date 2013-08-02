#!/bin/bash
out=$1
for i in {1..228}
do
if [ $((RANDOM % 2)) -eq 0 ] 
then 
  echo -ne "." >> $out
else
  echo -ne "@" >> $out
fi
done
