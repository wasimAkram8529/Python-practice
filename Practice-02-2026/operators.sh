#!/bin/bash

a=5
b=2
c=8

name="wasim"
age=23


d=3

# Unary Addition
((d++))
echo "value of d is ${d}"

((d = d + 1))
echo "value of d is ${d}"

((d += 1))
echo "value of d is ${d}"

# Uniray Subtraction
((d--))
echo "value of d is ${d}"

((d = d - 1))
echo "value of d is ${d}"

((d -= 1))
echo "value of d is ${d}"


# Unary Multiplication
d=3

((d = d * 2))
echo "value of d is ${d}"

((d *= 2))
echo "value of d is ${d}"

# Unary Division

d=20

((d = d / 2))
echo "value of d is ${d}"

((d /= 2))
echo "value of d is ${d}"

# Logical operator

# if [ $a -gt $b ] && [ $c -gt $b ]; then
#   echo "A and C is greater than B"
# elif [ $a -lt $c ] && [ $b -lt $c ]; then
#   echo "A and B is less than C"
# else
#    echo "C is greater than A and B"
# fi

# if [[ $a -gt $b  || $b -lt $c ]]; then
#   echo "A or C is greater than B"
# elif [[ $a -lt $c && $b -lt $c ]]; then
#   echo "A and B is less than C"
# else
#   echo "C is greater than A and C"
# fi

# if (( a > b && c > b )); then
#   echo "A and C is greater than B"
# elif (( a < c && b < c )); then
#   echo "A and B is less than C"
# else
#   echo "C is greater than A and B"
# fi

# numeric and comparision operator
# if [ $a -eq $b ]; then
#   echo "a is equal to b"
# elif [ $a -gt $b ]; then
#   echo "a is greater than b"
# else
#   echo "a is smaller than b"
# fi

# if [[ $a -eq $b ]]; then
#   echo "a is eqaul to b"
# elif [[ $a -gt $b ]]; then
#   echo "a is greater than b"
# else
#   echo "a is smaller than b"
# fi

# if [[ a -eq b ]]; then
#   echo "a is equal to b"
# elif [[ a -gt b ]]; then
#   echo "a is greater than b"
# else
#   echo "a is smaller than b"
# fi

# if (( a == b )); then
#   echo "a is equal to b"
# elif (( a > b )); then
#   echo "a is greater than b"
# else
#   echo "a is smaller than b"
# fi

# if [[ $name = "wasim" ]]; then
#   echo "User varified"
# else
#   echo "Invalid user"
# fi


