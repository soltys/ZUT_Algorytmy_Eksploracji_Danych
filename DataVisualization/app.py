# -*- coding: utf-8 -*-
__author__ = 'Paweł Sołtysiak'
import pandas as pd
import scipy.io.arff as arff
from sklearn import cross_validation
from sklearn.decomposition import PCA
import numpy as np
import scipy.io
import matplotlib.pyplot as plt

waveformData, waveformMeta = arff.loadarff(u'../Datasets/waveform-5000.arff')

df = pd.DataFrame(waveformData)
desc = df.values[:, -1]
df = df.drop('class', axis=1)

pca = PCA()

Y = pca.fit_transform(df.values)

for d in np.unique(desc):
    plt.plot(Y[d == desc, 0], Y[d == desc, 1], '.')

voteData, voteMeta = arff.loadarff(u'../Datasets/vote.arff')
df = pd.DataFrame(voteData)
desc = df.values[:, -1]
print df.replace('y', True)

df = df.drop('Class', axis=1)

pca = PCA()

Y = pca.fit_transform(df.values)

for d in np.unique(desc):
    plt.plot(Y[d == desc, 0], Y[d == desc, 1], '.')
plt.show()