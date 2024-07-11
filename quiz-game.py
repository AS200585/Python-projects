print("WELCOME TO THE COMPUTER QUIZ GAME")

playing = input("Do you want to play? ")

if playing.lower != "Yes":
    quit()

print("Okay! Let's start! :[)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower == "Central Processing Unit":
    print("That's Correct!")
    score += 1
else:
    print("Sorry, Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower == "Graphics Processing Unit":
    print("That's Correct!")
    score += 1
else:
    print("Sorry, Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower == "Random Access Memory":
    print("That's Correct!")
    score += 1
else:
    print("Sorry, Incorrect")

answer = input("What does ROM stand for? ")
if answer.lower == "Read Only Memory":
    print("That's Correct!")
    score += 1
else:
    print("Sorry, Incorrect")

print("Your score is " + str(score))