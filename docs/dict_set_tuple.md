# DICT
```
Dictionary in python is an unordered colection of data values, used to store values like a map. Unlike other data structure(which holds single value) dict stores key:value. 
```

**Creating a Dictionary**
```
Dictionary can be created by putting element in key:value format inside curl braces({}) seprated by comma. Values in dict can be any data type and can be repeted but key must be an immutable value and a non duplicate.
Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.
EX: 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
```

**methods**
```
copy()	They copy() method returns a shallow copy of the dictionary.

clear()	The clear() method removes all items from the dictionary.

pop()	Removes and returns an element from a dictionary having the given key.

popitem()	Removes the arbitrary key-value pair from the dictionary and returns it as tuple.

get()	It is a conventional method to access a value for a key.

dictionary_name.values()	returns a list of all the values available in a given dictionary.

str()	Produces a printable string representation of a dictionary.

update()	Adds dictionary dict2’s key-values pairs to dict

setdefault()	Set dict[key]=default if key is not already in dict

keys()	Returns list of dictionary dict’s keys

items()	Returns a list of dict’s (key, value) tuple pairs

has_key()	Returns true if key in dictionary dict, false otherwise

fromkeys()	Create a new dictionary with keys from seq and values set to value.

type()	Returns the type of the passed variable.

cmp()	Compares elements of both dict.
```