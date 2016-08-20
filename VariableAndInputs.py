Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myVariable

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    myVariable
NameError: name 'myVariable' is not defined
>>> myVariable = 30
>>> myVariable +30
60
>>> 
myVariable = 2
>>> myVa

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myVa
NameError: name 'myVa' is not defined
>>> myVariable
2
>>> myVariable ++3
5
>>> myVariable +++++5
7
>>> myVariable +++++++++++++2
4
>>> myVariable +===4334
SyntaxError: invalid syntax
>>> myVariable +== 34535
SyntaxError: invalid syntax
>>> myVariable
2
>>> myVariable ** 3
8
>>> myVariable
2
>>> value = input("Enter the value: ")
Enter the value: 50
>>> value
50
>>> value +20
70
>>> value = input("Enter the value ")
Enter the value Sugu

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    value = input("Enter the value ")
  File "<string>", line 1, in <module>
NameError: name 'Sugu' is not defined
>>> str = input("Enter the values")
Enter the values Sugu

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    str = input("Enter the values")
  File "<string>", line 1, in <module>
NameError: name 'Sugu' is not defined
>>> str = input("Enter the value: ")
Enter the value: Sugu

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    str = input("Enter the value: ")
  File "<string>", line 1, in <module>
NameError: name 'Sugu' is not defined
>>> str = input("Enter the value ")
Enter the value 'Sugu'
>>> str
'Sugu'
>>> str +30

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    str +30
TypeError: cannot concatenate 'str' and 'int' objects
>>> str +'Mad'
'SuguMad'
>>> str = int(input("Enter a value"))
Enter a value30
>>> str
30
>>> str = int(input("Enter a value"))
Enter a value'Sugu'

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    str = int(input("Enter a value"))
ValueError: invalid literal for int() with base 10: 'Sugu'
>>> str = float(input("Enter a value"))
Enter a value1
>>> str
1.0
>>> 
