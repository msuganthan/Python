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

#break, continue statements and else clause
print('break statements and else clasue')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, ' equals ', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')

print('continue statements and else clasue')
for n in range(2, 7):
    for x in range(2, n):
        if n % x == 0:
            print(n, ' equals ', x, '*', n//x)
            continue
        else:
            print(n, 'is a prime number')

#The pass statement does nothing
print('Pass statement')
while True:
    pass    # Busy-wait for keyboard interrupt (Ctrl+C)
