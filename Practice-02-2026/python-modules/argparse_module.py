import argparse

parser = argparse.ArgumentParser(description="This is argument parser")

parser.add_argument("name", type=str, help="Enter your name")
parser.add_argument("-a", "--age", type=int, help="Enter your age")
parser.add_argument("-v", "--verbose", action="store_true", help="Enabled verbose mode")

args = parser.parse_args()

print(args)
print(args.name)
print(args.age)
print(args.verbose)
