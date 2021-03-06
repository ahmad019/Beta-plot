# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:16:44 2018

@author: ahmad
"""


"""
graph plotting b/w two different values

"""
              
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
#from scipy.optimize import curve_fit
#import math as mp


j=0
i = int(input('enter the number of values: '))

x = np.ndarray(i, float)
y = np.ndarray(i, float)


while j<i:
     
    x[j] = input('enter x axis values: ')
    j +=1 

k=0
    
while k<i:
    
    y[k] = input('enter y axis values: ')
    k +=1
       
    
u1 = float(input('enter x uncertainity: '))
u2 = float(input('enter y uncertainity: '))
t = input('enter the title: ')
xl = input('Enter x-label: ')
yl = input('Enter y-label: ')
d = int(input('Enter degree of polynomial fit: '))
#sigma = raw_input('Enter the standard deviation: ')


plt.scatter(x,y, c='r')
plt.plot(x,y, 'g', label='Ball', linewidth=1)
plt.errorbar(x,y, xerr=u1, yerr=u2, ecolor='r' )
plt.grid()
plt.title(t) 
plt.xlabel(xl)
plt.ylabel(yl)
plt.show()

#ti = np.array(ti)   #converting into
#yi = np.array(yi)       # numpy array

#slope and intercept
stat = st.linregress(x,y)
slope = stat[0]
intercept = stat[1]
    
z = np.polyfit(x,y,d)   #data fitting
#z = np.polyfit(np.log(x), y, 1) #to take log of the values and fit ln(x)
#z = curve_fit(gaus,x,y) #to fit gaussian curve

f = np.poly1d(z)     #initializing a polynomial


x_new = np.linspace(x[0], x[-1], 50) #plotting the ploynomial deg 2
y_new = f(x_new)

#plt.xlim[-2,2]   #scale limits of 
#plt.ylim[-10,10]   # x and y axes

plt.plot(x,y,'o', x_new, y_new) #to plot the best fit curve
plt.title('Curve Fitting')
plt.text(x[0],y[1],'Slope=%.2f' %slope + '\nIntercept=%.2f' %intercept)
plt.show()

plt.title('Original Curve')
plt.plot(x_new,y_new, 'y')
plt.show()

