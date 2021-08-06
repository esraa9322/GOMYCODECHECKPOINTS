#QUESTION3
new_dictionary={}
n=int (input("ENTER A NUMBER : "))
if (n<1):
    print("INVALID INPUT")
else:
    for i in range(1,n+1,1):
        new_dictionary[i]=i*i
print(new_dictionary)
        