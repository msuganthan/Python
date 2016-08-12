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

#default argument
print('default argument')
def askOk(prompt, retries=2, remainder='Please try again!!!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(remainder)

askOk('Do you really want to quit?')
