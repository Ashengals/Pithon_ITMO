import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Задание 6
def cat_em(cat):
    dfr = pd.read_csv('emojis.csv')
    p=pd.Series(dfr.groupby('Category')['Category'].count())
    sum_p=(p.sum())
    c=list(p.index)
    if cat in c:
        return  print(f"категория {cat} составляет {p[cat]/sum_p*100}%")
    else:
        return print("такой категории нет")

cat_em("Animals & Nature")
cat_em("No_cat")

# Задание 7

def fn(a,b):
    df = pd.read_csv('BCT-USD.csv').set_index('Date')
    vybor= df.loc[a:b,['Open', 'Close']]
    print(vybor)
    plt.plot(vybor)
    plt.savefig('vybor.jpg')

fn('2021-10-21', '2021-10-24')
# Задание 8

# Задание 9