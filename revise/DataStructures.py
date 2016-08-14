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

