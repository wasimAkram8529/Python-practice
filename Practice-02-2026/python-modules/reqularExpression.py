# Literal string -> 'a', 'b'
# Metacharacter -> '.' match any character, '(backslash)d' match any digit
# Quantifier -> '*' zero or more, '+' one or more, '{n}' exact n occurence
# Anchors -> '^' match start of string, '$' match end of string
# Group -> ()
# classes -> []

# Literal string -> 'a', 'b'

import re

text = 'apple'
match = re.search('app', text)

print(match.group())

# metacharacter 
# '.' matches any single character
text = "cat"
match = re.search("c.t", text)

print(match.group())

# '\d' matches any digit (0-9)
text = "My number is 1234 5678"
match = re.search(r"\d+", text)

print(match.group())

text = "Hello_123"
print(re.findall(r"\w", text))

# Quantifier
# '*' zero or more occurence
text = "goooalgoooalglgoalgooal"
match = re.search(r"go*al", text)

print(match.group())

print(re.findall(r'go*al', text))

# '+' one or more occurence
text = "gooal"
match = re.search(r"go+al", text)

print(match.group())
print(re.findall(r'go+al', text))

# {n} exact n occurence
text = "aaa"
print(bool(re.search(r"a{3}", text)))

# {min, max}
text = "aaaa"
match = re.search(r"a{2,3}", text)

print(match.group())

# Anchor
# '^' match start of string
# '$' match start of string
text = "Hello world"
print(bool(re.search(r"^Hello", text)))  
print(bool(re.search(r"^world", text)))  
print(bool(re.search(r"world$", text))) 

text = "12345"
print(bool(re.search(r"^\d{5}$", text)))

# class ()
text = "Date: 21-02-2026"

match = re.search(r"(\d{2})-(\d{2})-(\d{4})", text)
print(match.group(0))
# print(match.group(1))
# print(match.group(2))

text = "abc123"
print(re.search(r"[a-zA-Z]", text).group())
print(re.findall(r'[a-zA-Z]', text))

text = "cat bat mat"
print(re.findall(r"[cbm]at", text))

email = "text123@gmail.com"

pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")


text = "I love apples. Apples are my favourite friut"

sub_result = re.sub(r"apples", "orange", text, flags=re.IGNORECASE)
print(sub_result)
