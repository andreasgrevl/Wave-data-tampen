import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

data = pd.read_csv("Tampen.txt",delimiter='\\t', engine = 'python')
data.to_csv('Tampen1.csv')


df = data[['YEAR', 'TOTALHS','TOTALTP']]

x = df['TOTALHS']

y = df['TOTALTP']

z = df['YEAR']


sns.set(style="darkgrid", rc={'figure.figsize':(12,8)})
sns.relplot(x="YEAR", y="TOTALHS",  kind="line", data=df);

