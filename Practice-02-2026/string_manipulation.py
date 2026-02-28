# slice
text = "Hello, world!"

text2 = '''
Hello World
Hello world
'''

print(text2)

n = len(text)
# print(text[-1])
# print(text[0])
# print(text[-2])
# print(n)
# print(text[0:5])
print(text[2:5])
print(text[::-1])

# strip
text = "     Python   "
print(text)
print(text.strip())

# split
text = "apple, banana, mango"
words = text.split(', ')
print(words)

# join

joined = " - ".join(words)
print(joined)

