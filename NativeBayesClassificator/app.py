from __future__ import division
# -*- coding: utf-8 -*-
__author__ = 'Paweł Sołtysiak'

import numpy as np
import pandas as pd


# import
class BayesZoo:
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

    def __init__(self):
        self.data = pd.read_csv(u'../Datasets/zoo.data', sep=',', names=self.column_names, header=None)
        self.data['type'].replace(self.numbers_names_mapping, inplace=True)
        pass

    def get_value_count_in_type(self, type_name, column_name, value):
        try:
            return self.data[self.data['type'].isin([type_name])][column_name].value_counts()[value]
        except:
            return 0

    def calculate_probality(self, type_name, column_name, value):
        type_count = self.get_value_count_in_type(type_name, column_name, value)
        data_count = self.data[self.data['type'].isin([type_name])][column_name].count()
        return type_count / data_count

    def classify(self, data):
        p = {key: 0 for (key) in self.type_names}
        for typeName in self.type_names:
            p_type = b.data['type'].value_counts().loc[typeName] / len(b.data)
            for columnName in self.column_names[1:-1]:
                p_class = self.calculate_probality(typeName, columnName, data[columnName])
                p_type *= p_class
            p[typeName] = p_type
        return p


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
