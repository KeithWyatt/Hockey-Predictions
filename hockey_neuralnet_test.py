from collections import Counter 
import numpy as np
import openpyxl as pyxl
import math
from sklearn.neural_network import MLPClassifier

#Code for getting the csv spreadsheet. Adjust the filepath according to your needs.
filepath = "C:\Users\Keith\Desktop\School\DataMining\Project\HockeyDataLight.xlsx"
wb = pyxl.load_workbook(filepath)
ws = wb.get_sheet_by_name('HockeyReference2009-2013')

X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

clf.fit(X, y)                         
MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
       beta_1=0.9, beta_2=0.999, early_stopping=False,
       epsilon=1e-08, hidden_layer_sizes=(5, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
       solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
       warm_start=False)

print clf.predict([[2., 2.], [-1., -2.]])