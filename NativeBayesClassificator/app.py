# -*- coding: utf-8 -*-
__author__ = 'Paweł Sołtysiak'

import numpy as np
import pandas as pd
# import

def readData():
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
    data = pd.read_csv(u'../Datasets/zoo.data', sep=',', names=columnNames, header=None)

    types = {
        1: 'mammal',
        2: 'bird',
        3: 'reptile',
        4: 'fish',
        5: 'amphibian',
        6: 'insect',
        7: 'shellfish',
    }
    data['type'].replace(types, inplace=True)
    return data


if __name__ == "__main__":
    df = readData()
    dataProps = {
        'sum': df.sum(),
        'count': df.count(),
        'mean': df.mean(),
        'std': df.std(),
    }
    print(dataProps['sum'])
    typeGroups = df.groupby('type')
    dataCount = typeGroups.agg(['sum', 'count', 'mean', 'std'])
    # print dataCount.loc['fish']
    #print dataCount.loc['mammal'].loc['legs']
    pass
