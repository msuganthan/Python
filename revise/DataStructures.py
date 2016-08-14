#list method
#append(x) -- Add an item to the end of the list. Equivalent to a[len(a):] = [x]
#extend(L) -- Extend the list by appending all the items in the given list. Equivalent to a[len(a):] = L
#list.insert(i, x) -- Insert an item at a given position. The first argument is the index of the element before which to insert.
#list.remove(x) -- Remove the first element from the list whose value is x.
#list.pop([i]) -- Remove the item at the given position in the list and return it. It no index specified list.pop() removes and return the last item in the list.
#list.clear() -- Remove all items from the list. Equivalent to a[:]
#list.index(x) -- Return the indes in the list of the first item whose is x
#list.count(x) -- Return the number of times x appears in the list
#list.sort(key=None, reverse=False) -- Sort the items of the list in plze
#list.reverse()
#list.copy() --Return the shallow copy of the list.

a = [66.25, 333, 333, 1, 1234.5]
print("==========INTIALLY====================")
print(a)
print("==========COUNT OPERATION 333=================")
print(a.count(333), a.count('x'))
print("==========INSERT OPERATION AT 2=================")
a.insert(2, -1)
print(a)
print("==========APPEND OPERATION===============")
a.append(333)
print(a)
print("==========INDEX 333 OPERATION===============")
print(a.index(333))
print("==========REMOVE 333 OPERATION===============")
a.remove(333)
print(a)
print("==========REVERSE OPERATION===============")
a.reverse()
print(a)
print("==========SORT OPERATION===============")
a.sort()
print(a)
print("==========POP OPERATION===============")
a.pop()
print(a)

print("=======LISTS AS STACK==========")
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print("=========AFTER APPEND===========")
print(stack)
print("=========AFTER POP===========")
print(stack.pop())
print(stack.pop())
print(stack)

print("============QUEUE=============")
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print("Initially: ",queue)
queue.append("Terry")
queue.append("Graham")
print("After append: ",queue)
queue.popleft()
queue.popleft()
print("After pop: ",queue)

print("==========List Comprehensions=========")
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
print("==========List Comprehension using lambdas=======")
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)
print("==========Concise List Comprehension========")
squares = [x ** 2 for x in range(10)]
print(squares)

#list comprehension consists of brackets containing an expression followed  by a for clause, then zero or more for or if clauses
print("====List comprehension using nested for====")
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print([x for x in [1, 2, 3]])

#create a new list with the values doubled
vec = [-4, -2, 0, 2, 4]
print("Doubled vector", [x*2 for x in vec])
print("filter in list", [x for x in vec if x>0])
print("apply function to all the elements",[abs(x) for x in vec])
freshfruit = ['   banana', '   loganberry',  'passion fruit']
print("call strip ", [weapon.strip() for weapon in freshfruit])
print("create a tuples ", [(x, x**2) for x in range(6)])
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("flatten ===>", [num for elem in vec for num in elem])

print("===========COMPLEX OPERATION==========")
from math import pi
print("complex operation using pi ",[str(round(pi, i)) for i in range(6)])


#ommitting nested operation

print("========DEL STATEMENT=========")
a = [-1, 1, 66.55, 333, 333, 1234.5]
print("Before del", a)
del a[0]
print("After del a[0]", a)
del a[2:4]
print("After del a[2:4]", a)
del a[:]
print("After del a[:]", a)

print("========TUPLES=============")
#tuples consists of number of elements separated by commas
t = 123, 456, 'hello'
print("tuple & t[0]", t, t[0])
print("======NESTED TUPLES========")
u = t, (1, 2, 3, 4, 5)
print("nested ", u)
#tuples are immutable

empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)
len(singleton)
singleton
x, y, z = t


