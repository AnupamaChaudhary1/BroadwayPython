#duck typing-  used in dynamic classes 
class Duck:
    def speak(self):
        return "Quack"
class Person:
    def speak(self):
        return "Hi"

def introduce(entity):    #method overriding where two classes have the same method name
    #feature that allows a subclass or child class to provide a specific implementation of
    #  a method that is already provided by one of its superclasses or parent classes
    print('Entity says: ', entity.speak())

d=Duck()
p=Person()
introduce(d)
introduce(p)