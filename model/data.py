import pandas as pd
import numpy as np

from pydantic import BaseModel


class Animal(BaseModel):
    hair: int
    feathers: int
    eggs: int
    milk: int
    airborne: int
    predator: int
    toothed: int
    backbone: int
    breathes: int
    venomous: int
    fins: int
    legs: int
    tail: int
    domestic: int
    class_type: int


class Dataset:
    def __init__(self):
        self.labels = pd.read_csv("data/class.csv").Class_Type
        self.zoo = pd.read_csv("data/zoo.csv")

    def animals(self):
        rows, columns = self.zoo.shape
        for i in range(rows):
            yield Animal.parse_obj(dict(zip(self.zoo.columns, self.zoo.loc[i])))
