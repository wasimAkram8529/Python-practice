#!/bin/bash

dir_name=$1
ext=$2

if [[ -z $dir_name || -z $ext ]]; then
  echo "Please enter a directory name and extension of file"
  exit 1
fi

file_count=$(find $dir_name -type f -name "*$ext" | wc -l | awk '{ print $1 }')
echo "File count of $ext extension in $dir_name is: $file_count"