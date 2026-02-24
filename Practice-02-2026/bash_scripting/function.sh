add(){
  local num1=$1
  local num2=$2
  local sum=$(( num1 + num2 ))

  echo "Sum of ${num1} and ${num2} is ${sum}"
  return $sum
}

subtract() {
  local num1=$1
  local num2=$2
  local diff=$(( num1 - num2 ))

  echo "All argument is $#"
  echo "Difference of ${num1} and ${num2} is ${diff}"
  return $diff
}

add 2 3
sum=$?

subtract 3 2
diff=$?

echo "${sum}"
echo "${diff}"


