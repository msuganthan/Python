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

#By adding this code at the end of you module __name__ == "__main__",
#you can use your file as a script as well as an importable module,
#because the code that parses the command line only runs if the
#module is executed as the "main" file

if __name__ == "__main__":
        import sys
        fib(int(sys.argv[1]))


#Module Search Path
#When a module named spam is imported, the interpreter first searches for a
#1. built-in module with that name
#2. if not found, it then searches for a file named spam.py in list of directories given by the variable sys.path
#sys.path is initailzed form these locations:
#        1. The directory containing the input script
#        2. PYTHONPATH
#        3. The installation-dependant default

#After initialization, Python programs can modify sys.path. The directory containing the script being run
#is placed at the beginning of the search path, ahead of the standard library path.

#Compiled Python files
#To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name

#Some tips for experts:

    #You can use the -O or -OO switches on the Python command to reduce the size of a compiled module.
         #The -O switch removes assert statements,
         #the -OO switch removes both assert statements and __doc__ strings.

        #A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file
