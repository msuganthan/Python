a = 0
while a<5:
    print(a)
    a+=1


b = 1
s = 0
print("Enter number to add to sum")
print("Enter 0 to quit")
while a != 0:
    print("Current sum : ", s)
    a = float(input("Number a"))
    s += a

print("Total Sum = ",s)

b = [2, 3, 4, 5, 6, 7, 8, 9]
for num in b:
    print("Number in list ",num)
