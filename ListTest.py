names = ["mark", "john", "july"]

names.append("sugu")

print(names[0])
print(names[-1])

print(names)

age = [1, 3, 4, 6]

names.extend(age)

print(names)

names.remove("mark")

print(len(names))
print(max(age))
print(names)
print(input("Press enter to exit"))
