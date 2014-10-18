from scipy.io import arff
import pandas as pd
import numpy as np
import pylab as plt




dd, meta = arff.loadarff('../Datasets/autos.arff')
attr_l =  [x[1] for x in dd]
print attr_l


df = pd.DataFrame(dd)
width = df['width']
city_mpg = df['city-mpg']
highway_mpg = df['highway-mpg']

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(width,city_mpg, '.')
cor_width_city_mpg = np.corrcoef(width,city_mpg)
print cor_width_city_mpg

ax2.plot(width,highway_mpg, '.')
cor_width_highway_mpg = np.corrcoef(width,highway_mpg)
print cor_width_highway_mpg
plt.show()
