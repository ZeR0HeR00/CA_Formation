#!/bin/bash
NAMES=( John Eric Jessica )
# write your code here
NUMBERS=( 1 2 3 )
STRINGS=('hello' 'world')
NumberOfNames=${#NUMBERS[@]}
second_name=${NAMES[${#NAMES[@]}-2]}

echo ${NUMBERS[@]}
echo ${STRINGS[@]}
echo The number of names listed in the NAMES array: $NumberOfNames
echo The second name on the NAMES list is: ${second_name}