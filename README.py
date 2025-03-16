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
    #affichage mot avec lettre devinées et lettres manquantes avec '*'
    affichage_mot= ' '.joint([lettre if lettre in lettres-trouves else '*' for in mot_a_deviner])
    print("mot a deviner :" + affichage_mot
    print("Lettres essayées:" + ',' , join(lettres_essayees))

    #dmd une lettre a l'utilisateur 
    lettre = input("Proposez une lettre:").upper()

        #verification lettre ou autre
    if len(lettre) != 1 or not lettre.isalpha(): #isalpha verifie si cest bien une lettre et non un chiffre ou symbole
       print("Veuillez entrer une seule lettr.")
       continue 

    # verification lettre deja proposer ou non 
    if lettre in lettres_essayees: 
       print("Vous avez déja essayé cette lettre."
       continue
