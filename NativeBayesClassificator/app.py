from __future__ import division
# -*- coding: utf-8 -*-

__author__ = 'Paweł Sołtysiak'

import pandas as pd
import scipy.io.arff as arff
from sklearn import cross_validation
import numpy as np

class MyBayes:
    def __init__(self, laplace=False):
        self.class_to_test = ''
        self.all_types = []
        self.data = ''
        self.bc = {}
        self.laplace = False

    def fit(self, all_data, class_to_test):
        self.data = all_data

        self.class_to_test = class_to_test
        self.all_types = class_to_test.unique()

        for column_name in self.data:
            self.bc[column_name] = pd.crosstab(all_data[column_name].values, self.class_to_test.values)

    def classify(self, testData):
        p = {key: 0 for (key) in self.all_types}

        for typeName in self.all_types:
            p_type = self.class_to_test.value_counts().loc[typeName] / len(self.data)

            for columnName in testData.keys():
                p_class = self.compute_probality(testData, typeName, columnName)
                p_type *= p_class
            p[typeName] = p_type
        return p

    def compute_probality(self, testData, typeName, columnName):
        p_class = self.bc[columnName]

        try:
            numerator = p_class[typeName].loc[testData[columnName]]
        except KeyError:
            return 1 / len(self.data)

        denominator = self.bc[columnName].sum().loc[typeName]

        if self.laplace:
            numerator += 1
            denominator += 1
        p_class = numerator / denominator
        return p_class


if __name__ == "__main__":
    data, meta = arff.loadarff(u'../Datasets/zoo.arff')
    data = pd.DataFrame(data)
    data = data.drop('animal', axis=1)

    b = MyBayes(laplace=False)
    # b.fit(data[1:-1], data['type'])

    # result = b.classify(human)
    #print result
    #print max(result, key=result.get)
    for alpha in np.logspace(-2, -0.1, 20):
        #alpha = 1-alpha
        X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(data, data['type'], test_size=alpha,
                                                                             train_size=1 - alpha, random_state=42)

        print alpha
        fitData = pd.DataFrame(X_train, columns=data.columns)

        yData = pd.DataFrame(Y_train, columns=['type'])
        fitData = fitData.drop('type', axis=1)
        #print len(fitData['hair'].values), len(fitData['type'].values)


        b.fit(fitData, yData['type'])

        # for test in np.arange(0,len(X_test)):
        #  print test






