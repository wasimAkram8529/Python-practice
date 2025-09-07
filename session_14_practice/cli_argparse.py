import argparse

parser = argparse.ArgumentParser(description="A sample demo of arg parser.", epilog="Thanks for using argparse!")

parser.add_argument("name", help="Enter your name")
parser.add_argument("-a", "--age", help="Enter your age")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode ON")
parser.add_argument("-d", "--debug", action="count", default=0, help="Set debug level")

arg = parser.parse_args()
print(arg)