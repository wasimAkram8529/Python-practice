from collections import deque
from queue import Queue

deque = deque()

deque.append("cus1")
deque.append("cus2")
deque.append("cus3")
deque.append("cus4")

print(deque.popleft())

queue = Queue()

queue.put("cus1")
queue.put("cus2")
queue.put("cus3")
queue.put("cus4")

print(queue.get())

# stack_of_plates = []
# stack_of_plates.append("plate1")
# stack_of_plates.append("plate2")
# stack_of_plates.append("plate3")
# stack_of_plates.append("plate4")

# reverse_stack = stack_of_plates[::-1]
# print(reverse_stack)

# while(len(stack_of_plates) != 0):
#   ele: str = stack_of_plates.pop()
#   print(f"{ele}")

# grocery_list = ["Milk", "Orange", 1, 2.2, True, 3+5j]
# print(grocery_list[1])
# print(grocery_list[::-1])
# grocery_list_2 = grocery_list;
# print(id(grocery_list), id(grocery_list_2))
# grocery_list_2.append(5)
# grocery_list.insert(2, 8)
# print(grocery_list)
# print(grocery_list.index(1))
# my_list = ["Apple", "Banana", "orange"]
# brothers_list = ["brinjal", "potato"]
# my_list.extend(brothers_list)
# print(my_list)

# num_list = [3, 6, 2, 8]
# n = len(num_list)
# i = 0

# while(i < n):
#   num_list[i] = num_list[i] * 2
#   i += 1

# print(num_list)

# print(num_list.pop(2))
# print(num_list)
# print(num_list.remove(6))
# print(num_list)

# new_num_list = [num * 4 for num in num_list]
# print(new_num_list)

# email_address = ["aj@gmail.com", "sj@yahoo.com", "rj@yahoo.com", "mj@gmail.com"]
# yahoo_mail = [email for email in email_address if "@yahoo.com" not in email]
# print(yahoo_mail)

# arr_2d = [[x, y] for x in [1, 2, 3, 4] for y in [6, 7, 8]]
# print(arr_2d)
# grocery_list_3 = grocery_list.copy() # deep copy
# print(id(grocery_list), id(grocery_list_3))
# print(grocery_list_3)
# grocery_list_3.append(7)
# print(grocery_list)
# print(grocery_list_3)