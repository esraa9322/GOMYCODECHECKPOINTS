#QUESTION1
found_numbers=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        found_numbers.append(i)
print(found_numbers)