#QUESTION6
import numpy as np 

firstMatrix=input("Original array1:")
Array1 = firstMatrix.split (",")

SecondMatrix=input("Original array2:")
Array2 = SecondMatrix.split (",")
info = np.array([Array1,Array2]).astype(int)
covarianceMatrix = np.cov(info)
print ("Covariance matrix of the said arrays:",covarianceMatrix)