purchase_price = int(input("Enter the purchase price: "))
selling_price = int(input("Enter the selling price: "))

diff = selling_price - purchase_price;

if diff >= 0:
  print(f"Profit and amount of profit is {diff}")
else:
  diff = -1 * diff
  print(f"Loss and amount of loss is {diff}")