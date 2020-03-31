#Print Formatting And Special Characters
**Use**
```
We use the print function to print values(passed variable value) on a console.
```
**Using + operator**
```
We can use the basic string operation of + to format the data.
string1 = "My name is"
string2 = "Python"
print(staring1 + " " + string2)
result: "My name is Python"
```
**Using multiple parameters**
```
We can pass multiple parameters in the print function. It does a concatenation of all the provided parameters.
print("My name is ", "Python")
result: "My name is Python"
```
**Using format method**
```
We can use the format method to format a string, It does a replacement of {} character with the respective parameter in the format method.
string1 = "Python"
print("My name is {}".format(string1))
```
**Using f keyword**
```
The simplest way to format a string is using f keyword
string1 = "My name is"
string2 = "Python"
print(f"{string1} {string2}")
```
#Special characters
```
Special characters in a string are the characters with special meanings.
Ex:. \(escape character), \n(line change), \t(tab)
```
**\\**
```
Backslash is a escape character. Using it Python interperstor ignores special meaning of the characters.
eg print('I\'m PPython')
```
