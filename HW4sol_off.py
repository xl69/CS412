#CS412 Homework 4 Solution

from sklearn.datasets import load_digits
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC, SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
import sklearn

def get_splits(n, k):

    permidx = np.random.permutation(n).tolist()
    per_bin = n // k
    prev = 0
    bins = []
    for i in range(per_bin, k * per_bin + 1, per_bin):
        bins.append(permidx[prev:i])
        prev = i
        
    if i < n: 
        for k, j in enumerate(range(i,n)):
            bins[k].append(permidx[j])
        
    return bins

def my_cross_val(method, X, y, k):

    if method == 'LogisticRegression':
        mymethod = LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial',
                                max_iter=5000)
    elif method == 'LinearSVC':
        mymethod = LinearSVC(max_iter=2000)
    elif method == 'SVC':
        mymethod = SVC(gamma='scale', C=10)
    elif method == 'RandomForestClassifier':
        mymethod = RandomForestClassifier(max_depth=20, random_state=0, n_estimators=500)
    elif method == 'XGBClassifier':
        mymethod = XGBClassifier()
        
    
    bins = get_splits(X.shape[0], k)
    
    acc = []
    for i in range(k):
        train_idx, test_idx = [], []
        for j in range(k):
            if i == j:
                test_idx += bins[j]
            else:
                train_idx += bins[j]
                
        mymethod.fit(X[train_idx,:], y[train_idx])
        ypred = mymethod.predict(X[test_idx,:])
        acc.append((ypred == y[test_idx]).sum() / len(test_idx))
        
    return 1 - np.array(acc)

def my_train_test(method, X, y, pi, k):
    if method == 'LogisticRegression':
        mymethod = LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial',
                                max_iter=5000)
    elif method == 'LinearSVC':
        mymethod = LinearSVC(max_iter=2000)
    elif method == 'SVC':
        mymethod = SVC(gamma='scale', C=10)
    elif method == 'RandomForestClassifier':
        mymethod = RandomForestClassifier(max_depth=20, random_state=0, n_estimators=500)
    elif method == 'XGBClassifier':
        mymethod = GradientBoostingClassifier()

    
    acc = []
    num_train = int(pi*X.shape[0])
    for i in range(k):
        permidx = np.random.permutation(X.shape[0]).tolist()
        mymethod.fit(X[permidx[:num_train],:], y[permidx[:num_train]])
        ypred = mymethod.predict(X[permidx[num_train:],:])
        acc.append((ypred == y[permidx[num_train:]]).sum() / len(ypred))
   
    return 1 - np.array(acc)

if __name__ == '__main__':
    digits = load_digits()
    X, y = digits.data, digits.target
    print(X.shape,y.shape,np.unique(y))
    
    print(y.shape[0])
    method = 'XGBClassifier'
    #my_cross_val(method, X, y, k=10)
    accuracyLR = my_train_test(method, X, y, pi=0.75, k=10)

    # report accuracy in each fold, and mean accuracy
    print(len(accuracyLR))
    print(np.mean(accuracyLR), np.std(accuracyLR))
    