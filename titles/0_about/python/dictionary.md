


## Find length of a dictionary
>  len(dict)
  ## delete value from a dictionary

```python
# delete an item from a dictionary -- if no value Raises error
del a_dict[color]

# this will not raise an error if element not found 
a_dict.pop(color, None)

```

## iterate over keys in dictionary
  
```python

d = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# prints keys of the dictionary
>>> for key in d:
...     print(key)
...
color
fruit
pet
>>> for item in d.items():
     print(item)
# ...returns 
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')

# getting key value pairs
>>> for key, value in d.items():
...     print(key, '->', value)


# gettins only the keys as array
>>> keys = d.keys()
print(keys) # this outputs dict_keys object
# dict_keys(['color', 'fruit', 'pet'])

>>> for value in d.values():
...     print(value)
# ...printing values
blue
apple
dog
```




## sort a dictionary
```python

d = {2:3, 1:89, 4:5, 3:0}
# get list of sorted dictnary values as tuples
a=sorted(d.items())
print(a)
>> [(1, 89), (2, 3), (3, 0), (4, 5)] #this is a list
# convert it back to dictionary
sd=dict(sorted(d.items()))
print(sd)
>> {1: 89, 2: 3, 3: 0, 4: 5} #this is a dictrionary
for k,v in sd:
     print( k, v)
```
> sorting by values
```python
a=dict(sorted(d.items(), key=lambda item: item[1]))
# Reversed
 a=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
```
 > sort by a lambda function
```py
from collections import OrderedDict


 sorted_mydict = OrderedDict(sorted(mydict.items(), key=lambda item: item[0]))

 ```