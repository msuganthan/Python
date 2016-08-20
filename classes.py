class Person:
    def __init__(self):
        self.id=id
        print("Our class is created")
    def __del__(self):
        print("Our class object is destroyed")
    def setFullName(self, firstName, lastName): #self points to class itself
        self.firstName = firstName
        self.lastName = lastName
    def printFullName(self0):
        return (self.firstName + " "+ self.lastName) 

personName=Person(1)
personName.setFullName("SUGU", "M")
personName.printFullName()
