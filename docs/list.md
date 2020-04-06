# List
```
List in python is a data structure which is mutable(changeable) ordered sequence of data. Each element in list is called an item and has an index.
Some of the comman list functions and method for comman actions are below

Sort - sort, sorted
Find - len, min, max, in , indexing, slicing, count
Insert/Remove - append, insert, extend, remove, pop
Sub-Lists -  Slicing, in-place, copy
Iteration - for lops, while loops
```

##### Sort
```.env
Sorting is any process of arranging items systematically.
For list python provides one funtction and one methods.

sort method:- 
list1 = [11,2,3,14]
list1.sort() it changes the list1 with the sorted value.
res = [2,3,11,14]

sorted function:-
sorted(list1) it doesn't sort the list1 value, but it returns a sorted list
```

##### Find
```
list1 = [11,100,-1,2,0,3]

len:- len is a function which returns length of list.
len(list1) = 6

count:- count() is an inbuilt function in Python that returns count of how many times a given object occurs in list.
list1 = [1, 1, 1, 2, 3, 2, 1]  
list1.count(1)
returns 4

min:- min function return minimum value from the list.
min(list1) = -1

max:- max function return maximum value from the list.
max(list1) = 100

in:- in return a boolean value whcih checks 
-1 in list1 Returns True
```

##### insert/remove
```
del[a : b] :- This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
lis = [2, 1, 3, 5, 4, 3, 8] 
el lis[2 : 5] 

pop() :- This method deletes the element at the position mentioned in its arguments.
pop(3) = [2,1,3,4,3,8]

insert(a, x) :- This method insert an elements at the specified position mentioned in its arguments. It takes 2 arguments position and element to add.
lis = [2, 1, 3, 5, 3, 8] 
lis.insert(3, 4) 

remove():- This method is used to delete the first occurance of number present in the argument.
lis.remove(1) = [2,3,5,3,8]

extent(list2):- This method take another list and it adds the items from the argument list into the object list.

clear() :- This function is used to erase all the elements of list. After this operation, list becomes empty.

reverse() :- This function reverses the elements of list.
```

##### SubLists
```
Sublist are the list from the provided list
list[start:end:steps]
```