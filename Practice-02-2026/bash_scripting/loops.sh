fruits=( "Apple" "Orange" "mango" )

echo "First fruit of fruits is ${fruits[0]}"
echo "First fruit of fruits is ${fruits[1]}"
echo "First fruit of fruits is ${fruits[2]}"
echo "All fruits: ${fruits[@]}"

for fruit in ${fruits[@]}; do
  echo "${fruit}"
done

i=0

while (( i <= 2 )); do
  echo "${fruits[$i]}"
  ((i += 1))
done