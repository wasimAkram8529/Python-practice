#!/bin/bash

url=$1
reciever_email=$2

if [[ -z $url ]]; then
  echo "Please enter a url"
  exit 1
fi

status_code=$(curl --head -s $url | awk '/^HTTP/  { print $2 }')
echo $status_code
if [[ $status_code == 200 || $status_code == 301 ]]; then
  echo "Website is working fine."
else
  if [[ -z $reciever_email ]]; then
      echo "Please enter reciever email address"
      exit 1
  fi
  echo "$url website is not working" | mail -s "Website not working" $reciever_email
  echo "Eamil sent successfully."
fi

