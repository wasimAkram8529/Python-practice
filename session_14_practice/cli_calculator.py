import argparse

parser = argparse.ArgumentParser(description="Calculator")

parser.add_argument("num1", type=float, help="Enter first number")
parser.add_argument("operator", choices=["add", "sub", "mul", "div", "rem"], help="Enter the operation you want to perform on numbers")
parser.add_argument("num2", type=float, help="Enter second number")

args = parser.parse_args()

num1 = args.num1
operator = args.operator
num2 = args.num2

match operator:
    case "add":
      print(f"Addition of {num1} and {num2} is: {num1 + num2}")
    case "sub":
      print(f"Subtraction of {num2} from {num1} is: {num1 - num2}")
    case "mul":
      print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")
    case "div":
      print(f"Division of {num1} by {num2} is: {num1 / num2}")
    case "rem":
      print(f"Reminder of {num1} divided by {num2} is: {num1 % num2}")
    case _:
        print("Invalid choice")