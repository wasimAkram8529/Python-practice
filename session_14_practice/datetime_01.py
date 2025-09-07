from datetime import datetime

now = datetime.now()
parse_str = now.strftime("%A, %B %d, %Y")
string_date = "07:09:2025 08:59"
obj_date = datetime.strptime(string_date, "%d:%m:%Y %H:%M")
print(parse_str)
print(obj_date)