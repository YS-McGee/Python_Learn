# Pandas

DataFrame: (2D) the whole sheet

Series: (1D) a column as a list

## Fatching csv

```python
data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()                   # convert to dict

>>> print(data)
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
```

## Get Data in Column

```python
# The same two ways
print(data.condition)
print(data['condition'])
```

## Get max temp of row

```python 
print(data[data.temp == data.temp.max()])
>>>
      day  temp condition
6  Sunday    24     Sunny
```

## Create DataFrame from Dict

```python
data_dict = {
    "students":["Amy", "James", "Franc"],
    "scores":[76, 58, 25]
}
df = pandas.DataFrame(data_dict)
df.to_csv('new_csv.csv')                    # Save the file
```