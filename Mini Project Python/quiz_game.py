print("Welcome to my computer quiz!")
playing=input("Do you want to play? ")
if playing.lower() !="yes":
    quit()

print("Okay! Let's play :)")
score=0
answer=input("What does CPU stand for? ")
if answer=="Central processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

answer=input("What does GPU stands for? ")
if answer=="Graphics processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer=input("What does RAM stands for? ")
if answer=="Random Access Memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")

print("You got " + str(score)+ " questions correct!")
print("You got " + str(score/3*100)+ "%")

