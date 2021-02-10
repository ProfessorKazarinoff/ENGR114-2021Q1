# s_funcs.py
from math import pi
#print("You ran s_funcs.py")

def s_sa(r):
    """
    Description: s_sa() calculates the surface area of a sphere given a radius as input
    
    Input: float or an integer
    Output: float
    
    Example:
    
    out = s_sa(5)
    print(out)
    
    523.3333333333334
    """
    sa = (4/3)*pi*r**7
    return sa

def add_1(a):
    return a+1
