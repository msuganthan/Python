#Informal Intro:
#===============

	#Numbers:
	#========
	
		>>> 17 / 3  # classic division returns a float
		5.666666666666667
		
		>>> 17 // 3  # floor division discards the fractional part
		5
		
		>>> 5 ** 2  # 5 squared
		25
		
		>>> 2 ** 7  # 2 to the power of 7
		128
		
		#In interactive mode, the last printed expression is assigned to the variable _.
		
		>>> tax = 12.5 / 100
		>>> price = 100.50
		>>> price * tax
		12.5625
		>>> price + _
		113.0625
		>>> round(_, 2)
		113.06
		
	#Strings:
	#========
	
	#If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings 
	
	>>> print(r'C:\some\name')  # note the r before the quote
	C:\some\name
	
	>>> 3 * 'un' + 'ium'
	'unununium
	
	>>> 'Py' 'thon'
	'Python'
	
	>>> prefix = 'Py'
	>>> prefix 'thon'  # can't concatenate a variable and a string literal
	  ...
	SyntaxError: invalid syntax
	>>> ('un' * 3) 'ium'
	  ...
	SyntaxError: invalid syntax
	
	>>> prefix + 'thon'
	'Python'
	
	>>> word = 'Python'
	>>> word[0]  # character in position 0
	'P'
	
	>>> word[-1]  # last character
	'n'
	
	>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
	'Py'
	
	>>> word[:2] + word[2:]
	'Python'
	
	>>> word[4:42]
	'on'
	>>> word[42:]
	''
	
	#Python strings cannot be changed — they are immutable. 
	
	>>> word[0] = 'J'
	  ...
	TypeError: 'str' object does not support item assignment
	>>> word[2:] = 'py'
	  ...
	TypeError: 'str' object does not support item assignment
	
	If you need a different string, you should create a new one:
	
	>>> 'J' + word[1:]
	'Jython'
	>>> word[:2] + 'py'
	'Pypy'
	
	>>> s = 'supercalifragilisticexpialidocious'
	>>> len(s)
	34
	
	#Lists:
	#======
	
	>>> squares = [1, 4, 9, 16, 25]
	>>> squares
	[1, 4, 9, 16, 25]
	
	>>> squares[:]
	[1, 4, 9, 16, 25]
	
	>>> squares + [36, 49, 64, 81, 100]
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
	#lists are a mutable type
	
	>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
	>>> 4 ** 3  # the cube of 4 is 64, not 65!
	64
	>>> cubes[3] = _  # replace the wrong value
	>>> cubes
	[1, 8, 27, 64, 125]
	
	>>> cubes.append(216)  # add the cube of 6
	>>> cubes.append(7 ** 3)  # and the cube of 7
	>>> cubes
	[1, 8, 27, 64, 125, 216, 343]
	
	#Assignment to slices is also possible
	
	>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	>>> letters
	['a', 'b', 'c', 'd', 'e', 'f', 'g']
	>>> # replace some values
	>>> letters[2:5] = ['C', 'D', 'E']
	>>> letters
	['a', 'b', 'C', 'D', 'E', 'f', 'g']
	>>> # now remove them
	>>> letters[2:5] = []
	>>> letters
	['a', 'b', 'f', 'g']
	>>> # clear the list by replacing all the elements with an empty list
	>>> letters[:] = []
	>>> letters
	[]
	
	#built-in function len() 
	
	>>> letters = ['a', 'b', 'c', 'd']
	>>> len(letters)
	4
	
	# possible to nest lists
	>>> a = ['a', 'b', 'c']
	>>> n = [1, 2, 3]
	>>> x = [a, n]
	>>> x
	[['a', 'b', 'c'], [1, 2, 3]]
	>>> x[0]
	['a', 'b', 'c']
	>>> x[0][1]
	'b'
	
	#Programming
	>>> # Fibonacci series:
	... # the sum of two elements defines the next
	... a, b = 0, 1
	>>> while b < 10:
	...     print(b)
	...     a, b = b, a+b
	
	>>> i = 256*256
	>>> print('The value of i is', i)
	The value of i is 65536
	
	#The keyword argument end can be used to avoid the newline after the output
	
	>>> a, b = 0, 1
	>>> while b < 1000:
	...     print(b, end=',')
	...     a, b = b, a+b
	...
	1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,