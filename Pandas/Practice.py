'''option 1'''
# with open("Pandas/weather_data.csv") as file:
#     CVS=file.readlines()
#     for row in CVS[1:]:
#         print(row.strip())

'''option 2'''

# import csv
# with open("Pandas/weather_data.csv") as file:
#     data=csv.reader(file)
#     temp=[]
#     for row in data:
#         if row[1] !='temp':
#             temp.append(int(row[1]))
#     print(temp)

'''option 3'''
# data=pd.read_csv("Pandas/weather_data.csv")
# print(data["temp"])
