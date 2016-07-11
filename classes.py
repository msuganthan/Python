class Person:
    def setFullName(self, firstName, lastName): #self points to class itself
        self.firstName = firstName
        self.lastName = lastName

    def printFullName(self):
        return (self.firstName + " "+ self.lastName) 

personName=Person()
personName.setFullName("SUGU", "M")
personName.printFullName()
