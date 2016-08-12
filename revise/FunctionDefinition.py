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
        if ok in ('y', 'ye', 'yes'): #test whether or not a sequence contain certain word or not
            return True
        if ok in ('n', 'no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(remainder)

askOk('Do you really want to quit?')

#Important warning: The default value is evaluated only once.
#This makes a difference when the default is a mutable object such as a list, dictionary
print('Important warning with mutable object')
def f(a, L=[]):
    L.append(a)
    return L


#Keyword Arguments
print('Functions can also be called using keyword arguments of the form kwarg=value')
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("voltage", voltage)
    print("state", state)
    print("action", action)
    print("type", type)

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def function(a):
    pass

#function(0, a=0)
