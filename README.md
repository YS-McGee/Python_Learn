# Heading

| Type                   | Public                | Internal            |
| ---------------------- | :-------------------- | :------------------ |
| Packages               | lower_with_under      |                     |
| Modules                | lower_with_under      | _lower_with_under   |
| Classes                | CapWords (PascalCase) | _PascalCase         |
| Exceptions             | PascalCase            |                     |
| Functions              | lower_with_under()    | _lower_with_under() |
| Global/Class Contents  | CAPS_WITH_UNDER       | _CAPS_WITH_UNDER    |
| Global/Class Variables | lower_with_under      | _lower_with_under   |

# Dict Comprehension

```python
import random

student_name = ["Alex", "Bernth", "Charlie", "David", "Elena", "Francesco"]
student_score = {name:random.randint(1,100) for name in student_name}
# print(student_score)
# {'Alex': 55, 'Bernth': 69, 'Charlie': 95, 'David': 60, 'Elena': 87, 'Francesco': 39}
student_pass = {name:score for (name,score) in student_score.items() if score >=60}
print(student_pass)
```
# Arguments
## *args:  Positional Arguments

```python
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
add(3, 5, 6, 10)

>>> 24
```

## **kwargs: Keyword Arguments

```python
def cal(n, **kwargs):
    for k,v in kwargs.items():
        print(k)
        print(v)
cal(2, add=3, mul=5)
```
# Exceptions
## The try, except, else, finally

```python
try: 
    # Do something that is exception-prone
    file = open('hahaha_not_a_virus.txt')
    a_dict = {"Key":"Value"}
    print(a_dict["aaa"])
except FileNotFoundError:
    # Do this if there was an exception
    file = open("hahaha_not_a_virus.txt", "w")
    file.write("{This is a flag}")
except KeyError as err_msg:
    print(err_msg)
else: 
    # Do this if there was no exceptions
    print(file.read())
finally: 
    # Do this no matter what
    file.close()
    print("File was closed")
```

## Raise custom exception

```python
if height > 3:
    raise ValueError("Human Height Should Not Be Over 3 Metres")
```