import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Задание 6
def cat_em(cat):
    dfr = pd.read_csv('emojis.csv')
    p=pd.DataFrame(dfr.groupby('Category')['Category'].count())
    p = p.rename({0: "A", 1: "B"})
    print(list(p.columns.values))
    # print(sum_p)
#     if any(p[0] == cat) == True:
#        return  print(f"категория {cat} ")
#     else:
#         return print("такой категории нет")
#
cat_em("Animals & Nature")

# Задание 7


# Задание 8

# Задание 9