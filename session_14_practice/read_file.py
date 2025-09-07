import argparse

def readFile():
  parser = argparse.ArgumentParser(description="Read file and count word lengths")
  parser.add_argument("filename", help="Enter name of the file you want to process")

  args = parser.parse_args()
  try:
    with open(args.filename, "r") as f:
      content = f.read()
      print(f"Content of {args.filename} is: \n{content}")
      words = content.split(" ")

      print(f"{words}")
      
      print(f"Total words in {args.filename} is: {len(words)}")
  except FileNotFoundError:
    print(f"Error: file {args.filename} not found.")

  except Exception as e:
    print(f"Unexpected error occur: {e}")

if __name__ == "__main__":
   readFile()