import random
import string
length = int(input(" Enter the length of password :"))
complexity = input("Enter the complexity level (simple, moderate , strong) : ")

if complexity == 'simple':
    char = string.ascii_lowercase
    
elif complexity == 'moderate':
    char = string.ascii_letters
    
elif complexity =='strong':
    char = string.ascii_letters + string.digits + string.punctuation
    
else:
    print("Invalid complexity level")
    
password = " ".join(random.choices(char, k=length))

print (" Your password is : ", password)
