import pandas

# data = pandas.read_csv('weather_data.csv')

# mon_temp = data[data.day == 'Monday'].temp
# print(float(mon_temp)*9/5 + 32)

data_dict = {
    "students":["Amy", "James", "Franc"],
    "scores":[76, 58, 25]
}
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv('new_csv.csv')