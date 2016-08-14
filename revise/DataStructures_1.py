#Set
#A set is an unordered collection with no duplicate elements. Basic uses include
#membership testing and eliminating duplicate entries.
#Set operation also support operation like union, intersection, difference and symmetric difference
#Curly braces or the set() function can be used to create sets.
print("=========SET=========")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("no duplicates ", basket)
print("=====FAST MEMBERSHIP TESTING=====")
print("'orange' in basket  ", 'orange' in basket )
print("'crabgrass' in basket  ", 'crabgrass' in basket )

print("========SET OPERATION=============")
a = set('abracadabra')
b = set('alacazam')
print("a  ", a)
print("b  ", b)
print("a-b", a-b)
print("a|b", a-b)
print("a&b", a&b)
print("a^b", a^b)


#dictionaries are indexed by keys, which can be any immutable type
print("===================DICTIONARIES==================")
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print("Dictionary tel ",tel)
print("Dictionary access by index ", tel['jack'])
del tel['sape']
print("after del tel['sape']", tel)
tel['irv'] = 4127
print(" list(tel.keys()) ",list(tel.keys()))
print(" sorted(tel.keys()) ",sorted(tel.keys()))
print("'guido' in tel ", 'guido' in tel)
print("'jack' not in tel ", 'jack' not in tel)


