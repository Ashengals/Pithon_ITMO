# Задание 1

import pandas as pd
import numpy as np

frame= pd.DataFrame(np.random.randint(5,10, size=(10,10)))
print(frame,"\n")


# Задание 2

frame=frame.rename({0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J"})
f1=frame
num=5
print(f1.loc[(f1[0]>num)&(f1[1]>num)&(f1[2]>num)&(f1[3]>num)&(f1[4]>num)&(f1[5]>num)&(f1[6]>num)&(f1[7]>num)&(f1[8]>num)&(f1[9]>num)])
print("\n")


# Задание 3
fr1= pd.DataFrame(np.random.randint(5,10, size=(10,10)), index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
print (fr1)
print('Razmernost:', fr1.shape)
print("\n")
print(list(fr1))
print("\n")
print("Srednee:",fr1.mean(axis=0).sum(axis=0)/10)
print("\n")
fr1.to_csv('fr1.csv')
print("File save")
# Задание 4
dfr= pd.read_csv('emojis.csv', sep=',', header=0, index_col='Subcategory')
# print(dfr.iloc[0])
sub_dfr=pd.DataFrame(dfr.groupby('Subcategory')['Rank'].sum())
res=sub_dfr.sort_values(['Rank'], ascending= False).head(1)
print(res)

# Задание 5

# Задание 6


# Задание 7


# Задание 8

# Задание 9