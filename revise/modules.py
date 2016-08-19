#Module is a file containing Python definitions and statements.
#Modules can be imported into other modules or into the main module

def fib(n):
	a, b = 0, 1
	while b < n:
		print(b, ' ')
		a, b = b, a + b
	print()

#Now enter the Python interpreter and import this module with the following command:
# import fibo
#fibo.fib(1000)
