# Master Notes

### String Methods

**Case Conversion**


```python
name = "Calvin"
```


```python
name.upper()
name.lower()
name.swapcase()
name.capitalize()
name.title()
```




    'Calvin'



**Strip** 

Removes the white space on either side of a string.


```python
name2 = "  Calvin      "
```


```python
name2.lstrip()
name2.rstrip()
name2.strip()
```




    'Calvin'




```python
name.replace("a", "e")
```




    'Celvin'



**Method Chaining** 

Performs multiple built in functions, but not all variations work together. 

**Replace**

1st argument is what's being replaced, 2nd argument is what it's being replaced with.


```python
name2.strip().replace("v", "*")
```




    'Cal*in'



**Startswith/Endswith**

Checks to see if the string starts/ends with that argument. Is case sensitive.


```python
name.startswith("Cal")
```




    True




```python
name.endswith("N")
```




    False



**In/Not In**

Checks for genereal inclusion/exclusion - whether the object on the left belongs/doesn't belong in the object on the right.


```python
"Z" in name
```




    False




```python
"Z" not in name
```




    True



# Lists


```python

```
