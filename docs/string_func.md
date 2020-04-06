# String Built-in functions

**Functions**
```
There are many built-in functions. we will only go through some of these
len, type, id, join, dir
```
**Methods**
```
Same as functions there are many methods of string. we will go through only some of them
capitalize, upper, lower, strip, find, split
```

_len_
```
This function is used for getting the length of string.
string1 = 'random'
len(string1) = 6
```
_type_
```
This function returns type of the object
string1 = 'random'
type(string1) = <class 'str'>
```
_id_
```
id function returns the address of the location where value of variable is stored.
string1 = 'random'
id(string1) = 1222568 (as a example value)
```
_join_
```
join function is used to join a list of string.
format "seprator of strings".join(list of string)
list_of_string = ['My', 'name', 'is', 'Python']
" ".join(list_of_string)
Here space is seprator
result will be "My name is Python"
```
_dir_
```
dir returns all the methods available for the variable.
```
_capitalize_
```
This method makes first letter of the word capital.
string1 = 'random'
string1.capitalize()
result- Random
```
_upper_
```
This method makes every character in upper case.
string1 = 'random'
string1.upper()
result:- 'RANDOM'
```
_lower_
```
This method makes every character in lower case.
string1 = 'RAndOm'
string1.lower()
result:- 'random'
```
_strip_
```
This method remove whitespaces from string.
string1 = ' RAndOm '
string1.strip()
result:- 'RAndOm'
```
_find_
```
This method return index of the letters from string.
string1 = ' RAndOm '
string1.find('A')
result:- 2
-1 will be result if letter is not there in the string.
```
_split_
```
split method is opposite of join function.
string1 = "My name is Python'
string1.split('')
['My', 'name', 'is', 'Python']
```