import pandas as pd
import numpy as np

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})
print(data.head())

data.loc[data['whoAmI']=='human','human']='1'
data.loc[data['whoAmI']!='human','human']='0'
data.loc[data['whoAmI']=='robot','robot']='1'
data.loc[data['whoAmI']!='robot','robot']='0'

print(data[['human','robot']].head())