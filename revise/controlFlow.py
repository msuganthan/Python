#if statement
x = input("Please enter an integer")
if x < 0:
    print(x, ' is negative number')
elif x == 0:
    print(' Zero ')
elif x > 0:
    print(x, ' is a positive number')


#for statement
words = ['cat', 'window', 'defenstrate']
for w in words:
    print(w, len(w))

#range functions
for i in range(3):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(5, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("Print range")
print(range(10))

print("List range")
print(list(range(10)))
