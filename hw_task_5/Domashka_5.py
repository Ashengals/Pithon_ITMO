# Задание 1

import pandas as pd
import numpy as np

frame= pd.DataFrame(np.random.randint(0,10, size=(10,10)))
print(frame)


# Задание 2

frame=frame.rename({0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J"})
print(frame)