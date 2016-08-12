#Defining a function
print('Fibonacci series')
def fibano(limit):
    a, b = 0, 1
    while a < limit:
        print(a)
        a, b = b , a + b

fibano(200)

#return a list from function
print('return list')
def Rfibono(limit):
    result = []
    a, b = 0, 1
    while a < limit:
        result.append(a)
        a, b = b, a + b
    return result

Rfibono(200)
