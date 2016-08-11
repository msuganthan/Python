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
