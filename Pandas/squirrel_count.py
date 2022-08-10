import pandas

df = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_sq_c = len(df[df["Primary Fur Color"] == "Gray"])
# print(gray_sq_c)
cin_sq_c = len(df[df["Primary Fur Color"] == "Cinnamon"])
blk_sq_c = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[gray_sq_c, cin_sq_c, blk_sq_c]
}
print(pandas.DataFrame(data_dict))