import pandas as pd

data=pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

grey_squirrel=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel=len(data[data["Primary Fur Color"]=="Black"])

squirrel_dict={
    'colors':['Gray','Red','Black'],
    'count':[grey_squirrel,red_squirrel,black_squirrel]
}

df=pd.DataFrame(squirrel_dict)
df.to_csv("squirrel_color_count.csv")
