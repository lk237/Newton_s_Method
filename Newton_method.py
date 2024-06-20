#CS_3308 Newton's method
#Group member: Leonel Kachie, Alessio Naji-Sepasgozar, Minh Anh Thai
#Solving 6(a) from Page 74

import math

# Define the function f(x) = e^x + 2^(-x) + 2*cos(x) - 6
def f(x):
    return math.exp(x) + 2**(-x) + 2*math.cos(x) - 6

# Define the derivative of f(x) = e^x - 2^(-x)*ln(2) - 2*sin(x)
def fprime(x):
    return math.exp(x) - 2**(-x)*math.log(2)  - 2*math.sin(x)

# Define the function for Newton's method 
def newtmethod(p0,TOL,n0):
    i = 1
    while i <= n0:
        # calculate the next approximation using Newton's
        p = p0 - f(p0)/fprime(p0)
        # To print every interation and estimation
        print(f"Iteration {i}: p = {p}")
        #check if the tolerance is meet 
        if abs(p - p0) < TOL:
            print(f"The procedure was successful after {i} iterations.")
            return p
        i += 1
        p0 = p
#Print a failed message if the function doesn't converge 
    print(f"The method failed after {n0} iterations.")
    return None

#Choose an initial guess within the given interval (1 < x < 2)
p0 = 1.5
#Set the tolerance to 10-5
TOL = 1e-5
#set the number of interation to 100
n0 = 100

#Call the newton method funtion
root = newtmethod(p0,TOL,n0)

#Check if root was found
if root is not None:
    print (f"The root found is: {root}")
else:
    print ("Root not found!")