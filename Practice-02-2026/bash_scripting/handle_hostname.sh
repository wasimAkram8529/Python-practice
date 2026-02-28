
if [[ -z $1 ]]; then
  echo "Please enter a file name to write hostname."
  exit 1
else
  hostname=$(hostname)
  echo $hostname > $1
  echo "Hostname is written successfully."
fi