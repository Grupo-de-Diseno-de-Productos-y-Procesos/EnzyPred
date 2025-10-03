import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier

def optimize_svm(X_train, y_train):
    '''
    Function to optimize the hyperparameters of a Support Vector Machine (SVM) model. It uses
    GridSearchCV to systematically search for the best combination of parameters.

    Inputs
        X_train: numpy.ndarray or pandas.DataFrame; The training feature set.
        y_train: numpy.ndarray or pandas.Series; The training labels or target values.

    Outputs
        Return: Tuple. Contains the best estimator (the trained model with the optimal parameters)
        and a dictionary with the best parameters found.
    '''
    param_grid = {
        'C': [0.1, 1, 10],
        'kernel': ['linear', 'rbf'],
        'gamma': ['scale', 'auto', 0.1]
    }
    grid_search = GridSearchCV(
        estimator=SVC(probability=True, random_state=42),
        param_grid=param_grid,
        cv=5,
        n_jobs=-1,
        scoring='accuracy'
    )
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_

def optimize_nn(X_train, y_train):
    '''
    Function to optimize the hyperparameters of a Neural Network (MLP) model. It uses
    GridSearchCV to find the best configuration for the hidden layers, learning rate, and alpha.

    Inputs
        X_train: numpy.ndarray or pandas.DataFrame; The training feature set.
        y_train: numpy.ndarray or pandas.Series; The training labels or target values.

    Outputs
        Return: Tuple. Contains the best estimator (the trained model with the optimal parameters)
        and a dictionary with the best parameters found.
    '''
    param_grid = {
        'hidden_layer_sizes': [(100, 50), (100,)],
        'learning_rate_init': [0.01, 0.1],
        'alpha': [0.001, 0.01],
        'activation': ['relu', 'tanh']
    }
    grid_search = GridSearchCV(
        estimator=MLPClassifier(max_iter=200, random_state=42),
        param_grid=param_grid,
        cv=5,
        n_jobs=-1,
        scoring='accuracy'
    )
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_

def optimize_gbc(X_train, y_train):
    '''
    Function to optimize the hyperparameters of a Gradient Boosting Classifier (GBC) model. It
    uses GridSearchCV to find the best settings for key parameters like n_estimators and max_depth.

    Inputs
        X_train: numpy.ndarray or pandas.DataFrame; The training feature set.
        y_train: numpy.ndarray or pandas.Series; The training labels or target values.

    Outputs
        Return: Tuple. Contains the best estimator (the trained model with the optimal parameters)
        and a dictionary with the best parameters found.
    '''
    param_grid = {
        'n_estimators': [50, 100],
        'learning_rate': [0.1, 0.2],
        'max_depth': [2, 3]
    }
    grid_search = GridSearchCV(
        estimator=GradientBoostingClassifier(random_state=42),
        param_grid=param_grid,
        cv=5,
        n_jobs=-1,
        scoring='accuracy'
    )
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_