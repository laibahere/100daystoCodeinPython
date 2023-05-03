print("WELCOME TO MY COMPUTER QUIZ")

playing =input("do you want to play?")
if playing.lower() != "yes" :
    quit()
print("Okay !Lets Play :)")
score = 0

answer1= input("What does CPU stands for?")
if answer1.lower() == "Central Processing Unit":
    print("Correct")
    score +=1
else:
    print("Wrong")

answer2= input("What does GPU stands for?")
if answer2.lower() == "Graphical Processing Unit":
    print("Correct")
    score +=1
else:
    print("Wrong")

answer3= input("What does RAM stands for?")
if answer3.lower() == "Random Access Memory":
    print("Correct")
    score +=1
else:
    print("Wrong")

answer4= input("What does PSUstands for?")
if answer4.lower() == "Power Supply":
    print("Correct")
    score +=1
else:
    print("Wrong")

print("you got" +str(score) + "question")
