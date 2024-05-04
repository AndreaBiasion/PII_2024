from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import numpy as np

class RandomForest:
    def __init__(self):
        self.Y = None
        self.X = None

    def classify(self, v1, v2):
        self.X = v1
        self.Y = v2

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.Y, test_size=0.3)

        model = RandomForestClassifier()

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)

        print('\nRandom forest stats')
        print(f'Accuracy: {accuracy}')
        print(f'F1: {f1:.4f}')
        print(f'Precision: {precision * 100}%')
        print(f'Recall: {recall * 100}%')
