# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are python container types. Both are ordered and indexed. Tuples are unique because their elements are immuatable--they cannot be changed by reassignment. Tuples can be used as dictionary keys, which must also be immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both mutable container types. However, lists are ordered (and, thus, can be indexed), while sets are not ordered. Sets are much better suited to functions associated with "set theory", like union, intersection, and difference.

>> Example union and intersection comparison:

```python
from copy import copy

# Determine union with only lists
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]

list_combined = copy(list_a) # preserve list_a
list_combined.extend(list_b)

list_union = list()
for element in list_combined:
	if not(element in list_union):
		list_union.append(element)

print(list_union) # [1, 2, 3, 4, 5, 6]


# Determine union with only sets--much easier!
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

set_union = set_a.union(set_b)

print(set_union) # set([1, 2, 3, 4, 5, 6])

# Items can be converted between lists and sets:
# list(set_union)
# set(list_union)

# Example using both--determine intersection
set_intersect = set(list_a).intersection(set(list_b)) # {3, 4}
list_intersect = list(set_intersect)                  # [3, 4]
```

>> Sets are faster than lists for determining membership because, like dictionaries, they are implemented with an index that is computed based on the value of the item. (This is called a hash table.)

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are a type of Python function that often does not have a name. Sometimes this function type is called "anonymous" or "inline." In contrast to regular functions that are declared with `def`, lambda functions are usually simpler and shorter (often one line of code).

```python
# Lambda functions and sorting

# Three lambda functions
name_reverser = lambda x: x[::-1]
second_letter_sort = lambda x: x[1]
length_sort = lambda x: len(x)

# A list of names
name_list = ['Frank', 'Zara', 'Joe']

# Reverse the names--this uses a list comprehension too
print([name_reverser(x) for x in name_list])     # ['knarF', 'araZ', 'eoJ']

# Alphabetical sorting (traditional)
print(sorted(name_list))                         # ['Frank', 'Joe', 'Zara']

# Sort by second letter of each name
print(sorted(name_list, key=second_letter_sort)) # ['Zara', 'Joe', 'Frank']

# Sort by length of each name
print(sorted(name_list, key=length_sort))         # ['Joe', 'Zara', 'Frank']
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

# - [ ] TODO: ANSWER ABOVE QUESTION

```python
## Lambda functions for filtering and mapping
get_day_abbreviation = lambda x: x[:3]

def get_day_number(day_name):
	day_mapper = {'Mon' : 0,
	              'Tue' : 1,
	              'Wed' : 2,
	              'Thu' : 3,
	              'Fri' : 4,
	              'Sat' : 5,
	              'Sun' : 6}

	return day_mapper[get_day_abbreviation(day_name)]

is_weekend = lambda day_name: get_day_number(day_name) >= 5


my_favorite_days = ['Fridat', 'Saturday', 'Sunday']

## List comprehension vs map
print([get_day_abbreviation(x) for x in my_favorite_days]) # ['Fri', 'Sat', 'Sun']

print(map(get_day_abbreviation, my_favorite_days))         # ['Fri', 'Sat', 'Sun']

## List comprehension vs filter
print([x for x in my_favorite_days if is_weekend(x)])      # ['Saturday', 'Sunday']

print(filter(is_weekend, my_favorite_days))                # ['Saturday', 'Sunday']

```

# -[ ] TODO add set comprehensions and dictionary comprehensions

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





