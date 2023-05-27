import random

NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 5

def poser_question():
    nb1 = random.randint(NB_MIN, NB_MAX)
    nb2 = random.randint(NB_MIN, NB_MAX)
    resultat = input(f"Calculez : {nb1} + {nb2} = ")
    if resultat == str(nb1 + nb2):
        #print("Réponse correcte")
        return True
    #else:
        #print("Réponse incorrecte")
    return False

nb_points = 0
for i in range(NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS}")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrecte")
    print()


print(f"Votre note est de : {nb_points} / {NB_QUESTIONS}")

if nb_points == NB_QUESTIONS:
    print("Excellent !")
elif nb_points == 0:
    print("Révisez vos maths !")
elif nb_points > int(NB_QUESTIONS / 2):
    print("Pas mal")
else: 
    print("Peut mieux faire")