# String

**How To Create**
```
string1 = 'This is how string created.'
string2 = "This is how string created.'
string3 = """This is how string created.
            And stores the line changes."""

All three methods are a valid way to create a string. In the third format, it stores the line changes also.

The first method we can use in case if we have a quote in our sting. For example

quote_string = 'This is how to store "Quote" in a string'

The second method can be used in the below example

second_string = "I'm learning how to create a string"

All the above functionality can be implemented with escape characters also

quote_string = "This is how to store \"Quote\" in a string"
second_string = 'I\'m learning how to create a string'
```

**Variables**
```
A variable is memory location reference which stores value.
string1 = "Store a new value."
Here variable string1 is an immutable variable. It means you cannot change the value of string1.
```

**Formating**

```
Addition of two string.

string1 = 'First String'
string2 = 'Second String'

string3 = string1 + string2
The result will be 'First StringSecond String'. You need to add space manually.
string3 = string1 + " " + string2
This is also a valid operation.
string1 = string1 + " " + string2
In the above expression string1 in left is different than string1 in right, as we know the string is Immutable. The first variable will not change, the only new variable will start referencing a new address.

```

**Indexing**
```
To learn indexing will see it with an example.
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
We will take the above example to explain slicing.
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