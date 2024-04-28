from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from numpy import random
import numpy as np

class DecisionTree:
    random.seed(0)
    def __init__(self):
        self.Y = None
        self.X = None

    def classify(self, v1, v2):
        # Unisci i valori del dizionario in un array 2D
        self.X = v1

        # Assicurati che v2 sia un array numpy
        self.Y = v2

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.Y, test_size=0.3)

        model = DecisionTreeClassifier()

        model.fit(X_train, y_train)

        Prediction = model.predict(X_test)

        errori = accuracy_score(y_test, Prediction)

        print(errori)
