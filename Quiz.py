import time
import os
import time
print(
  "Welcome to this project made by Reyansh Varshney and this is a quiz. Let's see how much you'll score out of 4!"
)
choice = input("Are you ready? (yes/no):")
score = 0
total_questions = 4
os.system("cls||clear")
if choice.lower() == 'yes':
  person_name = input("What is your name? ")
  os.system("cls||clear")
  answer1_by_the_user = input("Who is the current Prime minister of Britain?:")
  if answer1_by_the_user.lower() == "rishi sunak":
    score += 1
    print("Dear, ", person_name, "You're correct")
  else:
    print(
      "Dear, ", person_name,
      "Wrong answer, no problem try the next question😔. See all the correct answers at the end of the quiz!"
    )
  time.sleep(3)
  os.system("cls||clear")
  answer2_by_the_user = input("Which company owns ChatGPT?:")
  if answer2_by_the_user.lower() == "openai":
    score += 1
    print("Dear, ", person_name, "Good attempt! Continue like this!")
  else:
    print(
      "Dear, ", person_name,
      "Wrong answer, no problem try the next question😔. See all the correct answers at the end of the quiz!"
    )
  time.sleep(3)
  os.system("cls||clear")
  answer3_by_the_user = input("Who invented the Powerpoint?:")
  if answer3_by_the_user.lower() == "robert gaskins":
    score += 1
    print("Dear, ", person_name, "Very Good!")
  else:
    print(
      "Dear, ", person_name,
      "Wrong answer😔. See all the correct answers at the end of the quiz!")
  time.sleep(3)
  os.system("cls||clear")
  answer4_by_the_user = input("Who is the current President of India")
  if answer4_by_the_user.lower() == "draupadi murmu":
    score += 1
    print("Dear, ", person_name, " Awsome you're correct!")
  else:
    print(
      "Dear, ", person_name,
      " Wrong answer😔. See all the correct answers at the end of the quiz!")
  time.sleep(3)
os.system("cls||clear")
print("You've scored ", score, "/", total_questions,
      "See the correct answers below⬇️")
print("""Q1.Who is the current Prime minister of Britain? Answer: Rishi Sunak
 Q2.Which company owns ChatGPT?  Answer: OpenAI
 Q3.Who invented the Powerpoint? Answer:Robert Gaskins
 Q4. Who is the current President of India? Answer: Draupadi Murmu""")
marks = score / total_questions * 100
print("You were ", marks, "% accurate!")
print("Thanks for playing this game")
time.sleep(60)
quit()