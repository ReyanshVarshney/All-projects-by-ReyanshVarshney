import random
import time
print("Welcome to Dice roll project by Reyansh Varshney a student of 5th class")

while True:
    print(""" 
    Press 1 to spin the dice
    Type farewell to close the program""")
    userchoicefarewellorspindice = int(input("Type your answer. For any help see the above text"))
    if userchoicefarewellorspindice == 1:
        dicenumber=random.randint(1,6)
        print("Your dice is giving the number...")
        time.sleep(dicenumber)
        if dicenumber == 1:
            print("   ")
            print(" . ")
            print("   ")
        if dicenumber == 2:
            print(".  ")
            print("   ")
            print("  .")
        if dicenumber == 3:
            print(".  ")
            print(" . ")
            print("  .")
        if dicenumber == 4:
            print(". .")
            print("   ")
            print(". .")
        if dicenumber == 5:
            print(". .")
            print(" . ")
            print(". .")
        if dicenumber == 5:
            print(". .")
            print(". .")
            print(". .")
        
            
        
        
        print("You're number is ", dicenumber, "!")
        print(""" 
        Credits:
        Code Writer: Reyansh Varshney (A student of Class 5th)""")
    else:
        print("👋, I hope you'll open this project again, If this was by mistake you've to open this project again or else quit! ")
        print("10")
        time.sleep(1)
        print("9")
        time.sleep(1)
        print("8")
        time.sleep(1)
        print("7")
        time.sleep(1)
        print("6")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        quit(10)




