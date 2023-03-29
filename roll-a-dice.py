import random
response="y"
response=input("Please enter 'y' for rolling the dice and 'n' for exiting: ")
print(response)

if response =="y":
    no = random.randint(1,6)

elif response=="n":
    no = 0

if no==0:
    print("Thanks for using this dice")
elif no==1:
    print("-----")
    print("     ")
    print("  0  ")
    print("     ")
    print("-----")

elif no==2:
    print("-----")
    print("    0")
    print("     ")
    print("0    ")
    print("-----")

elif no==3:
    print("-----")
    print("    0")
    print("  0  ")
    print("0    ")
    print("-----")
    
elif no==4:
    print("-----")
    print("0   0")
    print("     ")
    print("0   0")
    print("-----")

elif no==5:
    print("-----")
    print("0   0")
    print("  0  ")
    print("0   0")
    print("-----")
        
else:
    print("-----")
    print("0   0")
    print("0   0")
    print("0   0")
    print("-----")

print(response)

    