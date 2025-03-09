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
    
while essais_restants >0
    # affiche le mot avec les lettres devinées et les lettres manquantes en '_'
    affichage_mot= ' '.joint([lettre if lettre in lettres-trouves else '_' for in mot_a_deviner])
    print("mot a deviner :" + affichage_mot
    print("Lettres essayées:" + ',' , join(lettres_essayees))

    #demande une lettre a l'utilisateur 
    lettre = input("Proposez une lettre:").upper()

    #verifie que l'entrée est une lettre unique 
    if len(lettre) != 1 or not lettre.isalpha():
       print("Veuillez entrer une seule lettr.")
       continue 

    # verifie si la lettre a déja été proposée 
    if lettre in lettres_essayees: 
       print("Vous avez déja essayé cette lettre."
       continue
