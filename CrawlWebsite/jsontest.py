import pandas as pd
import json
import re

with open('interparktmp.txt', encoding='UTF-8-sig') as json_file:
     data = json.load(json_file)

del data["code"]
del data["message"]

# print(data["data"]['orderDeliveries'][0])
print("-"*100)
# print(data["data"]['orderDeliveries'][1])
# print(data)
data1 = data["data"]['orderDeliveries'][0]
data2 = data["data"]['orderDeliveries'][1]

stack = 0



df = pd.DataFrame.from_records(data["data"]['orderDeliveries'][0], index=[0])
df = df.append(data["data"]['orderDeliveries'][1] , ignore_index=True)

print(df)

df.to_csv('interpark.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')
# for i in range(2):
#     info = data["data"]['orderDeliveries'][i]
#     df = pd.DataFrame.from_records(info, index=[0])
#
# df.to_csv('interpark.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')

# df = pd.DataFrame.from_records(data1, index=[0])
# df.to_csv('interpark.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')
# df = pd.DataFrame.from_records(data2, index=[0])
# df.to_csv('interpark.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')

# print(df)
# df.to_csv('interpark.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')
