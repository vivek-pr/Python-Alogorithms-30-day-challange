# Class
```
Class is a user defined blueprint or prototype from which objects are created. Classes provides a means to enacapsulate data and functionality together.
Class has attributes and methods. It is user defined datastructure.

In python classes are created using 'class' keyword. Attributes are the variable attached with class. Attributes are always public and can be used using . keyword.
```

###### Class Objects
```
An object is a instance of class. Object uses the blueprint to shape itself assigns values to attributes and uses methods to do the operations.

An object consist 3 things state, behavior, identity.
State:- Attributes of object
Behavior:- Methods of objects
Identity:- Name of objects

How To define a class:
class Animal:
    def __init__(self, name):
        self.name =  name #Attribute
        
    def get_name(self): # Method
        return self.name

Create a new object

animal = Animal('jackel')
```

###### OOP in Python
```
OOP is a programming pattern which helps in structuring the program such that properties and behavior are bundle into individual objects.
```

