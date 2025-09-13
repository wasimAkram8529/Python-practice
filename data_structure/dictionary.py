d = {"name":"Ajay", "email":"aj@gmail.com", "contact": 1234}

d["alpha"] = "beta"
keys = d.keys()
print(keys)
values = d.values()
print(values)
items = d.items()
print(items)
d_shallow_copy = d
d_deep_copy = d.copy()

print(id(d), id(d_shallow_copy))
print(id(d), id(d_deep_copy))
d.update({"name2": "Wasim"})
print(d)
print(d.get("name3"))

students = ["Arun", "Ajay", "Bijay"]
marks = [80, 95, 100]

for i in zip(students, marks):
    print(i)