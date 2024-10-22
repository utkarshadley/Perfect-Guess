import random 
n=random.randint(1,100)
a=-1
guess=0
while(a!=n):
    guess+=1
    a=int(input("Guess the Number:"))
    if(a>n):
        print("Select a smaller number")
    else:
        print("Select Higher Number")
        
print(f"Congratulations! You guessed the number in {guess} attempts")
        
