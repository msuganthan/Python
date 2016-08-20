class Parent:
    value1="this is value 1"
    value2="this is value 2"


class Parent1:
    value1="this is value 1"
    value2="this is value 2"  

class Child (Parent, Parent1):
    pass

parent_= Parent()
print(parent_.value1)
child_ = Child()
print(child_.value2)
