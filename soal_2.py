import numpy as np

def f(x):
    return x**3 + x**2 - 34*x - 56

def bisection_method(f, xl, xu, tol=1.0):
    iterasi = 0
    xr_old = xl
    print(f"{'Iter':<5} {'XL':<8} {'XU':<8} {'XR':<8} {'f(XR)':<10} {'Et (%)':<10}")
    
    while True:
        xr = (xl + xu) / 2.0
        fxr = f(xr)
        iterasi += 1
        
        if iterasi == 1:
            et = np.nan
        else:
            et = abs((xr - xr_old) / xr) * 100

        print(f"{iterasi:<5} {round(xl,2):<8} {round(xu,2):<8} {round(xr,2):<8} {round(fxr,2):<10} {'' if iterasi == 1 else round(et,2)}")

        if f(xl) * fxr < 0:
            xu = xr
        else:
            xl = xr
        
        if iterasi != 1 and 0 <= et < tol:
            break

        xr_old = xr

    print(f"\nAkar pendekatan: {round(xr,2)}")
    return xr

akar = bisection_method(f, xl=-2, xu=3)
