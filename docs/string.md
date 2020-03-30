# String

**How To Create**
```
string1 = 'This is how string created.'
string2 = "This is how string created.'
string3 = """This is how string created.
            And stores the line changes."""

All the three methods are valid way to create a string. In third format it stores the line changes also.

First method we can use in case if we have a quotes in our sting. For example

quote_string = 'This is how to store "Quote" in a string'

Second method can be used in below example

second_string = "I'm learning how to create a string"

All the above functionality can be implemented with escape characters also

quote_string = "This is how to store \"Quote\" in a string"
second_string = 'I\'m learning how to create a string'
```

**Variables**
```
Variable is memory location refrence which stores value.
string1 = "Store a new value."
Here variable string1 is a immutable variable. It means you cannot change the value of string1.
```

**Formating**

```
Addition of two string.

string1 = 'First String'
string2 = 'Second String'

string3 = string1 + string2
Result will be 'First StringSecond String'. You need to add a space manually.
string3 = string1 + " " + string2
This is also a valid operation.
string1 = string1 + " " + string2
In above expresion string1 in left is diffrent than string1 in right, as we know string is Immutable. First variable will not change, only new variable will start refrencing a new address.

```

**Indexing**
```
To learn indexing will see it with a example.
           0123456789
string1 = "ALGORITHMS"
           -10-9-8-7-6-5-4-3-2-1   
string1[0] = string[-10]
string1[1] = string[-9]
Assignemnet to a string index will give type error.

string1[0] = '1' #will give TypeError Exception      
```

**Slicing**
```.env
We will take above example to explain slicing.
           0123456789
string1 = "ALGORITHMS"
           -10-9-8-7-6-5-4-3-2-1   
slicing format [start(default=0): stop+1(default=len(string)): steps(default=1]
Let suppose we want ALGO from string1
string1[0:4:1] or string1[:4:1] or string1[:4] or string1[:4:]

To print things in reverse order we can use steps value as negative
string[::-1] = 'SMHTIROGLA'  

To print all the odd digit characters
String[::2] = 'AGRTM'         
```