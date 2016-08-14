#looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#using enumerate, the position index and corresponding value can be retrieved at the same time using enumerate() function
for k, v in enumerate(knights.items()):
    print(k, v)

#To loop over two or more sequences at the same time,

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#reversed loop
for i in reversed(range(1, 10, 2)):
     print(i)


#sorted loop
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
     print(f)

#Comparing Sequence
#https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
