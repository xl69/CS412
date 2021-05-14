import numpy as np
import random
import math
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def get_splits(n, k):
    x = np.arange(n)
    random.shuffle(x)
    return np.array_split(x, k)

def my_cross_val(method, X, y, k):
    
    X = np.array(X)
    y = np.array(y)
    
    folds = get_splits(len(y), k)
    
    X_split = []
    y_split = []
    
    for fold in folds:
        fold = np.array(fold)
        X_split.append(X[fold])
        y_split.append(y[fold])
        
    
    accuracy = []
    
    for i in range(k):
        print(i)
        X_train = np.concatenate(np.delete(X_split, i, 0))
        y_train = np.concatenate(np.delete(y_split, i, 0))
        X_test = X_split[i]
        y_test = y_split[i]
        if (method == 'SVC'):
            mySVC = SVC(gamma='scale', C=10)
            mySVC.fit(X_train, y_train)
            y_pred = mySVC.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        if (method == 'LinearSVC'):
            myLinearSVC = LinearSVC(max_iter = 2000)
            myLinearSVC.fit(X_train, y_train)
            y_pred = myLinearSVC.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        if (method == 'LogisticRegression'):
            myLR = LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial', max_iter = 5000)
            myLR.fit(X_train, y_train)
            y_pred = myLR.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        if (method == 'XGBClassifier'):
            myXGB = XGBClassifier()
            myXGB.fit(X_train, y_train)
            y_pred = myXGB.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        if (method == 'RandomForestClassifier'):
            myRF = RandomForestClassifier(max_depth = 20, random_state=0, n_estimators=500)
            myRF.fit(X_train, y_train)
            y_pred = myRF.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        
    return accuracy

def my_train_test(method, X, y, pi, k):
    print(len(X), len(y))
    accuracy = []
    X = np.array(X)
    y = np.array(y)
    x = np.arange(len(y))
    
    for i in range(10):
        random.shuffle(x)
        Train_index, Test_index = np.array_split(x, [math.floor(len(y)*0.75), len(y)])[:2]


        X_train = X[Train_index]
        y_train = y[Train_index]

        X_test = X[Test_index]
        y_test = y[Test_index]
        
        
        if (method == 'SVC'):
            mySVC = SVC(gamma='scale', C=10)
            mySVC.fit(X_train, y_train)
            y_pred = mySVC.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        if (method == 'LinearSVC'):
            myLinearSVC = LinearSVC(max_iter = 2000)
            myLinearSVC.fit(X_train, y_train)
            y_pred = myLinearSVC.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        if (method == 'LogisticRegression'):
            myLR = LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial', max_iter = 5000)
            myLR.fit(X_train, y_train)
            y_pred = myLR.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        if (method == 'XGBClassifier'):
            myXGB = XGBClassifier()
            myXGB.fit(X_train, y_train)
            y_pred = myXGB.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
        if (method == 'RandomForestClassifier'):
            myRF = RandomForestClassifier(max_depth = 20, random_state=0, n_estimators=500)
            myRF.fit(X_train, y_train)
            y_pred = myRF.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            accuracy.append(1 - acc)
    return accuracy
