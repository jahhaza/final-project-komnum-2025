import numpy as np

x = 5

xi = (np.sqrt( x*x*x/-6 + 19*x/6 + 14))

for i in range(5):
    ea = np.abs(xi - x)*100/xi
    x = (np.sqrt( x*x*x/-6 + 19*x/6 + 14))
    xi = (np.sqrt( xi*xi*xi/-6 + 19*xi/6 + 14))
    print ("Iterasi", i+1, "=", np.round(x,2))
    print ("Ea =", np.round(ea,2),"%")
    print ("")