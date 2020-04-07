#### Iterator
```.env
Iterators are data structures that can be used with for loop.
Ex:. list, set, dict, tuple.
These all the data structures has one common property. They all have implement __iter__ (for intilization) and __next__ (for getting next value) methods.
```

#### Generator
```
Generators are used to create iterators, but with diffrent approch. It returns an Iterable with access of one items at a time.

When an iteration over a set of item starts using the for statement, the generator is run. Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

Ex:--
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
```