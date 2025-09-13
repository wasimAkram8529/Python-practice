str = "       wasim  "
print(str.strip())
print(str)

string ="Hii Wasim"
string = string + " how are you"
print(string)

str_arr = string.split(" ")
print(str_arr)
print(type(str_arr))
table = "Name\tAge\tGrade\nWasim\t23\tA\nPuneeth\t23\tA"
print(table)

name = "Wasim"
greeting = "Hello %s, wish you a wonderful day"%name
print(greeting)

print(len(string))
print(string.replace("Hii", "Hello"))
print(string)

print(string.capitalize())
print(string.title())
print(string.swapcase())
print(string)
print("how" in string)
str_list = ["KKKH", "Magic", "Singham", "Aalishan"]
print(sorted(str_list))
str_list.sort()
print(str_list)
count = string.count("H")
print(count)
print(string[::1])
print(string[::-1]) # reverse the string

string = "I'm a student"
print(string)

string = """
Hii wasim
How are you buddy
"""

print(string)


string = "Hii wasim \nhow are you buddy"
print(string)



char = "A"
print(ord(char))
char = "a"
print(ord(char))
char = "0"
print(ord(char))
char = "h"
print(ord(char))
print(chr(66))
print(chr(98))