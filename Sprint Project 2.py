
#David Ritchie
#A quiz game based on FGCU with multiple answer choices incoporated.



#Converts the 0 into a number so we can add scores
score = 0
score = int(score)

#Asks user for their name
name = input("What is your name?")
name = name.title()
print("""Hello {}, welcome to David's Quiz Game! 
You will be presented with 5 questions.
Enter the appropriate number to answer the question
Good luck!""".format(name))

#Question1
print("""What is the name of a building in South Village?
1. Green field 
2. Swamp Hall 
3. Griffins Hall 
4. Eagle Hall""")

answer1 = "4"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question2
print("""What is the name of the dinner in South Village?
1. Eagle Dinning 
2. Sovi Dinning 
3. Osprey Dinning 
4. Boardwalk""")

answer2 = "2"
response2 = input("Your answer is:")

if (response2 != answer2):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question3
print("""How many Housing buildings are in South Village?
1. Seven 
2. Five 
3. Eight 
4. Four""")

answer3 = "1"
response3 = input("Your answer is:")

if (response3 != answer3):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question4
print("""What is the name of FGCU mascot?
1. Richard the Hawk
2. Tony the Seagull
3. Azul the Eagle
4. Otto the Sparrow""")

answer4 = "3"
response4 = input("Your answer is:")

if (response4 != answer4):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question5
print("""What is a FGCU slogan?
1. Beaks High
2. Wings Up
3. Tails High
4. Wings Raised""")

answer5 = "2"
response5 = input("Your answer is:")

if (response5 != answer5):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1

print("Your total score is " + str(score) + " out of 5")
print("Thank you for playing {}, goodbye!".format(name))