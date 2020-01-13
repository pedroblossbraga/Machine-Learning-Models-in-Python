# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:01:54 2019

@author: pedro.braga

=====================================
 Random Number Polynomial Regression
=====================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randint

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def main():
    x,y =[],[]
    print(' ', '\n',
          'The program generates a given input quantity of random numbers,',
          'and then fits it to a polynomial regression in a given input degree',
          '\n',' ')
    Z = int(input('How many random numbers to generate? '))
    for i in range(Z):
        x.append(i)
        y.append(randint(0,100))
    x = np.array(x)
    y = np.array(y)
    y = y.reshape(-1,1)
    x = x.reshape(-1,1)

    poly_regressor(x, y)
    

    
def poly_regressor(x, y):
    k = int(input('Qual o grau da regressão? '))
    poly=PolynomialFeatures(degree=k)
    poly_x = poly.fit_transform(x)

    regressor=LinearRegression()
    regressor.fit(poly_x,y)
    
    plt.scatter(x,y,color='red', label='pontos reais')
    plt.legend(loc='best')
    plt.plot(x,regressor.predict(poly.fit_transform(x)),color='blue', label='regressao')
    plt.legend(loc='best')
    plt.show()

while True:
    try:
        print(__doc__)
        main()
        q = str(input('Continue? Y / N'+'\n'))
        if q.replace(' ','') == 'N' or q.replace(' ','') == 'n':
            print('End...')
            break
    except Exception as e:
        print(e)

    
