import re

text = "Hello, welcome to the world of regexp."
text_2 = "The rain in spain stays maily in the plain."
text_3 = "I love apples, Apples are my favourite."

match_result = re.match(r"Hello", text)
search_result = re.search(r"plain", text_2)
all_match = re.findall(r"ain", text_2)
sub_string = re.sub(r"apples", "Oranges", text_3, flags=re.IGNORECASE)

print(match_result)
print(search_result)
print(all_match)
print(sub_string)