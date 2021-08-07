#QUESTION7
import math as ma
C=50 
H=30 
D = input ("Enter comma separated integers: ")
list1 = D.split (",")
for i in range(0,len(list1),1):
    q= (2*C*int(list1[i]))/H
    Q=ma.floor(ma.sqrt(q))
    print("Q for this integer --> " ,Q)
    #print(Q , end= ",")