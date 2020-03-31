#Numbers, Math, Typecasting and Input
###**Numbers**
```
Python provides 3 different types of objects for numbers.
- int
- float
- complex
```
###### _int_
```.env
An integer is a whole number
The valid operation which can be done with int
- Addition operator(+)
Adding multiple integers return an Integer value
eg: 2+3 = 5 is a integer value

-Subtraction operator(-)
Similar to addition subtracting multilple integers return a Integer value
eg:. 2-3 = -1 is a type integer field

- Multiplication operator(*)
Multiplying multiple integers also returns an Integer value
eg: 2*3 = 6 is a integer field

- Division operator(/ or //)
Divison using "/" returns float, but using "//" returns Integer.
eg:- 10/3=3.33 is a float
10//3 = 3 is a integer

- Modulo operator(%)
Modulo operator is used for getting reminders
eg:- 10%3 = 1

- Power operetaor(**)
ex:- 2**2 = 4

- math Library
Math library provides us many of the basic operations on integer, eg:- pow, log
eg:- math.pow(2,2) = 4
math.log2(1000)
For all the operation user has to import math library

- random library
the random library is used to generate random numbers
random.randit(start_digit, end_digit)

```

###**Casting**
```
Casting is a function used to convert a data type from one form to another if it is compatible.
ex:- s1 = "12"
Here s1 is a string, but since 12 is an integer we can easily cast it to integer
int(s1)=12
other casting operators
str(), float(), int()
```

###**Getting input from user**
```.env
We use the input keyword to get input from the command-line.
Eg:
input("Please enter a input")

All the input provided in the command line comes in string format.

```
