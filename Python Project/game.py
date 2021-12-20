print("welcome to my computer quiz")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay Let's Play: ")
score = 0
answer = input("Who discovered Protons? ")
if answer.lower() == "ruther ford":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer= input("What does ‘Xylem’ in plants do? ")
if answer.lower() == "transport water":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer= input("Which is the ‘class’ of Octopus? ")
if answer.lower() == "cephalopod":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    

answer = input("What does Big Bang Theory explain? ")
if answer.lower() == "origin of universe":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("Who is the author of ‘Origin of Species’? ")
if answer.lower() == "charles darwin":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What kind of mosquito carries malaria? ")
if answer.lower() == "anopheles mosquitoes":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Name the smallest Ocean. ")
if answer.lower() == "arctic ocean":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Which day is celebrated as World Consumer Rights Day? ")
if answer.lower() == "march 15":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is Light year? ")
if answer.lower() == "unit of distance":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Which is the sacred book of Buddhists? ")
if answer.lower() == "tripitakas":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Cataract is the disease of _. ")
if answer.lower() == "eye":
    score += 1
    print("Correct")
else:
    print("Incorrect")

answer = input("What is the SI unit of Force? ")
if answer.lower() == "newton":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Who is the author of ‘Wings of Fire’? ")
if answer.lower() == "a.p.j. abdul kalam":
    print("Correct")
    score += 1
else:
    print("Incorrect")

ansnwer = input("Who is the father of Economics? ")
if answer.lower() == "adam smith":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the common name of Sodium Carbonate? ")
if answer.lower() == "washing soda":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got",score,"question correct")