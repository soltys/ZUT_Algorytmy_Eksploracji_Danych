from __future__ import division
# -*- coding: utf-8 -*-
__author__ = 'Paweł Sołtysiak'

import numpy as np
import pandas as pd

# import
class BayesZoo:
    numbersToNamesMapping = {
        1: 'mammal',
        2: 'bird',
        3: 'reptile',
        4: 'fish',
        5: 'amphibian',
        6: 'insect',
        7: 'shellfish',
    }
    typeNames = numbersToNamesMapping.values()
    columnNames = [
        'animalName',
        'hair',
        'feathers',
        'eggs',
        'milk',
        'airborne',
        'aquatic',
        'predator',
        'toothed',
        'backbone',
        'breathes',
        'venomous',
        'fins',
        'legs',
        'tail',
        'domestic',
        'catsize',
        'type'
    ]

    def __init__(self):
        self.readData()
        pass

    def calculateBinaryProbality(self, typeName, columnName):
        sumForType = self.typeGroupsAgg.loc[typeName].loc[columnName].loc['sum']
        classCount = self.data[columnName].sum()
        return sumForType / classCount

    def calculateValuesProbality(self, typeName, columnName):
        typeStd = self.typeGroupsAgg.loc[typeName].loc[columnName].loc['std']
        mean = self.typeGroupsAgg.loc[typeName].loc[columnName].loc['mean']
        denominator = np.sqrt(2 * np.pi * typeStd ** 2)
        value = (1 / denominator) * np.exp(-(6 - mean) ** 2 / 2 * typeStd ** 2)

        return value


    def calculateProbality(self, typeName, columnName, value):
        sameInType = 0
        try:
            sameInType = self.data[self.data['type'].isin([typeName])][columnName].value_counts()[value]
        except:
            pass
        dataCount = self.data[self.data['type'].isin([typeName])][columnName].count()
        return sameInType / dataCount
    def readData(self):

        self.data = pd.read_csv(u'../Datasets/zoo.data', sep=',', names=self.columnNames, header=None)
        self.data['type'].replace(self.numbersToNamesMapping, inplace=True)

        self.typeGroups = self.data.groupby(['type'])
        self.typeGroupsAgg = self.typeGroups.agg(['sum', 'count', 'mean', 'std'])


    def classify(self, data):
        pForEachType = {key: 0 for (key) in self.typeNames}

        for typeName in self.typeNames:
            pType = b.data['type'].value_counts().loc[typeName] / len(b.data)
            for columnName in self.columnNames[1:-1]:
                pForClass = self.calculateProbality(typeName, columnName, data[columnName])
                pType *= pForClass
            pForEachType[typeName] = pType
        return pForEachType


if __name__ == "__main__":
    b = BayesZoo()
    sample = "0,1,1 0,1,0 1,0,1 1,0,0 2,1,0 0"

    human = {
        'hair': 1,
        'feathers': 0,
        'eggs': 0,
        'milk': 1,
        'airborne': 0,
        'aquatic': 0,
        'predator': 1,
        'toothed': 1,
        'backbone': 1,
        'breathes': 1,
        'venomous': 0,
        'fins': 0,
        'legs': 2,
        'tail': 0,
        'domestic': 1,
        'catsize': 0,

    }
    result = b.classify(human)
    print max(result, key=result.get)
