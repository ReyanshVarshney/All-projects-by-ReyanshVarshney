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
        time.sleep(6)
        print("You're number is ", dicenumber, "!")
        print(""" 
        Credits:
        Code Writer: Reyansh Varshney (A student of Class 5th)""")





