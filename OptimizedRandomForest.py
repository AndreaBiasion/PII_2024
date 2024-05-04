from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

class RandomForestOptimized:
    def __init__(self):
        self.best_estimator_ = None
        self.best_params_ = None


    def train(self, X_train, y_train):
        # Definizione del modello Random Forest
        rf = RandomForestClassifier()

        # Definizione del dizionario degli iperparametri da testare
        param_grid = {
            'n_estimators': [50, 100, 200],  # Numero di alberi nell'ensemble
            'max_depth': [None, 10, 20, 30],  # Profondità massima degli alberi
            'min_samples_split': [2, 5, 10],  # Numero minimo di campioni richiesti per suddividere un nodo
            'min_samples_leaf': [1, 2, 4]  # Numero minimo di campioni richiesti per essere in una foglia
        }

        # Definizione della Grid Search con cross-validazione a 5 fold
        grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='f1', n_jobs=-1)

        # Esecuzione della Grid Search sul set di dati di addestramento
        grid_search.fit(X_train, y_train)

        # Salvataggio dei migliori iperparametri trovati
        self.best_estimator_ = grid_search.best_estimator_
        self.best_params_ = grid_search.best_params_

    def evaluate(self, X_test, y_test):
        # Valutare le prestazioni del modello con i migliori iperparametri
        y_pred = self.best_estimator_.predict(X_test)

        # Calcolare le metriche di valutazione
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)

        print('\nRandom Forest Optimized stats')
        print(f'Accuracy: {accuracy}')
        print(f'F1: {f1:.4f}')
        print(f'Precision: {precision*100}%')
        print(f'Recall: {recall*100}%')
