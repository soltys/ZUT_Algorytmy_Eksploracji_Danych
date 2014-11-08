from __future__ import division
# -*- coding: utf-8 -*-

__author__ = 'Paweł Sołtysiak'

import pandas as pd

numbers_names_mapping = {
        1: 'mammal',
        2: 'bird',
        3: 'reptile',
        4: 'fish',
        5: 'amphibian',
        6: 'insect',
        7: 'shellfish',
    }
type_names = numbers_names_mapping.values()
column_names = [
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


class MyBayes:



    def __init__(self):
        self.class_to_test = ''
        self.all_types = []
        self.data = ''
        self.bc = {}
        self.laplace = False
        pass

    def fit(self, all_Data, class_to_test, laplace=False):
        self.data = all_Data

        self.class_to_test = class_to_test
        self.all_types = class_to_test.unique()

        self.laplace = laplace

        for column_name in self.data.columns[1:-1]:
            self.bc[column_name] = pd.crosstab(data[column_name].values, class_to_test.values)


    def get_value_count_in_type(self, type_name, column_name, value):
        try:
            value_count = self.bc[type_name][column_name]['values'][value]
        except:
            value_count = 0

        if self.laplace:
            value_count += 1

        return value_count

    def get_data_count(self, type_name, column_name):
        pass

    def calculate_probality(self, type_name, column_name, value):
        type_count = self.get_value_count_in_type(type_name, column_name, value)
        data_count = 1
        return type_count / data_count

    def classify(self, indata):
        p = {key: 0 for (key) in self.all_types}

        for typeName in self.all_types:
            p_type = self.class_to_test.value_counts().loc[typeName] / len(self.data)

            for columnName in indata.keys():
                p_class = self.bc[columnName]
                p_class = p_class[typeName].loc[indata[columnName]] / self.bc[columnName].sum().loc[typeName]
                p_type *= p_class
            p[typeName] = p_type
        return p


if __name__ == "__main__":
    b = MyBayes()
    data = pd.read_csv(u'../Datasets/zoo.data', sep=',', names=column_names, header=None)
    data['type'].replace(numbers_names_mapping, inplace=True)

    b.fit(data[1:-1], data['type'])

    cross = pd.crosstab(data['legs'].values, data['type'].values)

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
    result = 0
    result = b.classify(human)
    print result
    print max(result, key=result.get)
