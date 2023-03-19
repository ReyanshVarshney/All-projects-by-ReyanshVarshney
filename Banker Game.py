import random
import time
print(""" ______________________________________________________________________
|                                                                      |
| ==================================================================== |
| |%/^\\%&%&%&%&%&%&%&%&{ Federal Reverse Note }%&%&%&%&%&%&%&%&//^\%| |
| |/inn\)===============------------------------===============(/inn\| |
| |\|UU/              { UNITED STARES OF AMERICA }              \|UU/| |
| |&\-/     ~~~~~~~~   ~~~~~~~~~~=====~~~~~~~~~~~  P8188928246   \-/&| |
| |%//)     ~~~_~~~~~          // ___ \\                         (\\%| |
| |&(/  13    /_\             // /_ _\ \\           ~~~~~~~~  13  \)&| |
| |%\\       // \\           :| |/ ~ \| |:  3.21  /|  /\   /\     //%| |
| |&\\\     ((iR$)> }:P ebp  || |"- -"| ||        || |||| ||||   ///&| |
| |%\\))     \\_//      sge  || (|e,e|? ||        || |||| ||||  ((//%| |
| |&))/       \_/            :| `._^_,' |:        || |||| ||||   \((&| |
| |%//)                       \\ \\=// //         || |||| ||||   (\\%| |
| |&//       R265402524K       \\U/_/ //   series ||  \/   \/     \\&| |
| |%/>  13                     _\\___//_    1932              13  <\%| |
| |&/^\      Treasurer  ______{ Frankly }_______   Secretary     /^\&| |
| |/inn\                ))--------------------((                /inn\| |
| |)|UU(================/ ONE HUNGERED DOLLARS \================)|UU(| |
| |{===}%&%&%&%&%&%&%&%&%a%a%a%a%a%a%a%a%a%a%a%a%&%&%&%&%&%&%&%&{===}| |
| ==================================================================== |
|______________________________________________________________________|

Welcome to Banker Roulette

Get ready you may need to pay for the meal, Be ready!""")
names_of_people=input("Give the names of the people who want to pay for the meal" " seperate them with a comma and a space")
names_final= names_of_people.split(", ")
a=len(names_final)-1
num=random.randint(0,a)
person=names_final[num]
print(f"{person} is going to buy the meal today")
print("Please show honesty")
time.sleep(10)
quit()
