#QUESTION4
word=str(input("Enter a string: "))
num=int(input("Enter a number: "))
if (num<0) or (num>=len(word)):
    print("INVALID NUMBER")
else:
    
    new_word=word.replace(word[num],"")
    print("The new string is: ",new_word)
