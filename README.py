# pendu hello 
import random

def dessinPendu(nb):
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab [nb]

def liste_de_mots():
    l=[]
    with open("tous_lesLmots.txt,"r") as fichier:
        for i in fichier:
            l.append(i.strip())
    return l

def choisir_hasard(fichier):
    return random.choice(fichier).upper()

#Fonction principale

def jeu_pendu():
    mots = liste_de_mots()
    mot_a_deviner = choisir_hasard(mots)
    lettres_trouvees = ()
    lettres_envoyees = ()
    essais_restants = 6

    print("bienvenue au jeu du pendu!")
    print(dessinPendu((0))

    while essais_restants > 0:
        affichage_mot=' '.join((lettre if lettre in lettres_trouvees else'_'for lettre in mot_a_deviner))
        print("mot a deviner:" + affichage_mot)
        print("lettres essayees:"+','.join(lettres_essayees))
