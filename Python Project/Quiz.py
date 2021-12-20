def one_word_question(score=0):
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
    
    return score

def mcq(score=0):
    print("Q.1 Which crop is sown in the most important area in India?")
    print("(A) Rice       (B) Wheat")
    print("(C) Sugarcane  (D) Maize")
    answer = input("Enter the choice ")
    if answer.lower() == "a":
        print("correct")
        score += 1
    else:
        print("Incorrect")
    
    print("Q.2 Eritrea, which became the 182nd member of the United Nations in 1993, is on the continent of")
    print("(A) Asia    (B) Africa")
    print("(C) Europe  (D) Australia")
    answer = input("Enter the choice ")
    if answer.lower() == "b":
        print("correct")
        score += 1
    else:
        print("Incorrect")

    print("Q.3 Which of the subsequent personalities gave ‘The Laws of Heredity? ")
    print("(A) Robert Hook  (B) G.J. Mendel")
    print("(C) Darwin       (D) Harvey")
    answer = input("Enter the choice ")
    if answer.lower() == "b":
        print("correct")
        score += 1
    else:
        print("Incorrect")

    print("Q.4 Garampani sanctuary is found at")
    print("(A) Junagarh, Gujarat    (B) Diphu, Assam")
    print("(C) Kohima, Nagaland     (D) Gangtok, Sikkim")
    answer = input("Enter the choice ")
    if answer.lower() == "b":
        print("correct")
        score += 1
    else:
        print("Incorrect")

    print("Q.5 Who is understood as “The Saint of Gutters”? ")
    print("(A) Baba Amte   (B) Teresa")
    print("(C) Anna Hazare (D) None of those")
    answer = input("Enter the choice ")
    if answer.lower() == "b":
        print("correct")
        score += 1
    else:
        print("Incorrect")

    print("Q.6 that of the subsequent disciplines is Nobel prize awarded?" )
    print("(A) Physics and Chemistry             (B) Physiology or Medicine")
    print("(C) Literature, Peace and Economics   (D) All of the above")
    answer = input("Enter the choice ")
    if answer.lower() == "d":
        print("correct")
        score += 1
    else:
        print("Incorrect")

    print("Q.7 Grand Central Terminal, Park Avenue, NY is that the world’s ")
    print("(A) largest railroad station  (B) highest railroad station")
    print("(C) longest railroad station  (D) None of the above")
    answer = input("Enter the choice ")
    if answer.lower() == "a":
        print("correct")
        score += 1
    else:
        print("Incorrect")

    print("Q.8 Name the one that was also referred to as Deshbandhu.")
    print("(A) S. Radhakrishnan (B) G.K. Gokhale")
    print("(C) Chittaranjan Das (D) Madan Mohan Malviya")
    answer = input("Enter the choice ")
    if answer.lower() == "c":
        print("correct")
        score += 1
    else:
        print("Incorrect")

    print("Q.9 FFC stands for ")
    print("(A) Foreign Finance Corporation    (B) Film Finance Corporation")
    print("(C) Federation of Football Council (D) None of the above")
    answer = input("Enter the choice ")
    if answer.lower() == "b":
        print("correct")
        score += 1
    else:
        print("Incorrect")

    print("Q.10 Which of the subsequent national parks isn’t listed during a UNESCO World Heritage site? ")
    print("(A) Kaziranga  (B) Keoladeo")
    print("(C) Sundarbans (D) Kanha ")
    answer = input("Enter the choice ")
    if answer.lower() == "d":
        print("correct")
        score += 1
    else:
        print("Incorrect")
    
    return score

print("welcome to my computer quiz")

playing = input("Do you want to play? ")
if playing.lower() == "no":
    quit()
else:
    print("Okay Let's Play: ")
    score = 0
    answer = input(" A)one word quiz B)mcq ")
    if answer.lower() == "a":
        score = one_word_question(score)
    elif answer.lower() == "b":
        score = mcq(score)
    
    print("you got",score,"correct question")