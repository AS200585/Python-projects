name = input("Type your name : ")
print("welcome to your adventure, " + name + ".")

answer = input("You are on a dirt road, it has come to an end. You can move either left or right. Which way would you like to go? ")

if answer == "left":
    answer = input("You came to a river, you can walk around it or swim across it. Yould you like to walk around or swim across it? Type walk to walk or swim to swim : ")
    if answer == "walk":
        print("You walked through kilometres of jungle and got lost and ran out of water.")
    elif answer == "swim":
        print("You start swimming through the river but got caught and eaten by an alligator.")
    else:
        print("Invalid option. You lose :{")
elif answer == "right":
    answer = input("You saw a car but could not find its keys. Eventually, you find the keys and after resting throught the night, you drive away. You survived.")
else:
    print("Invalid path. You lost.")