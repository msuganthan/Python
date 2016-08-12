#Defining a function
print('Fibonacci series')
def fibano(limit):
    a, b = 0, 1
    while a < limit:
        print(a)
        a, b = b , a + b;

fibano(200)
