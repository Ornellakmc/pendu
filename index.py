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
    =============
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
    l=[] #liste vide pour tous les mots 
    with open("tous_lesLmots.txt","r") as fichier: #ouvre fichier mode lecture
        for i in fichier:  
            l.append(i.strip()) #parcours chaque ligne et on enleve les espaces et les sauts de ligne et on ajt dans la liste l
    return l #on retoune la liste complete des mots

def choisir_hasard(fichier):
    return random.choice(fichier).upper()  #choisir un mot au hasard dans la liste 

#Fonction principale du jeu 
def jeu_pendu():
    while True: # boucle infini qui permet au joueur de jouer autant de fois qu'il veut tant qu'il ny a pas de break 
        mots = liste_de_mots()  #cherche une fonction non definie
        mot_a_deviner = choisir_hasard(mots)  #choisit un mot au hasard a deviner
        lettres_trouvees = []   #liste des lettres trouvees par les joueurs 
        lettres_envoyees = []   #listes des lettres deja essayees
        essais_restants = 6     #nombre dessais maximum avant de perdre

        print("bienvenue au jeu du pendu!")  
        print(dessinPendu((0)))  #affiche le dessin du pendu correspondant a 0 erreurs
    
        while essais_restants >0:   #tant que le joueur a des essais restants
            #affiche le mot avec les lettres trouvees et des lettres manquantes avec '*'
            affichage_mot=' '.join([lettre if lettre in lettres_trouvees else '*' for lettre in mot_a_deviner])
            print("mot a deviner :", affichage_mot)
            print("Lettres essayées:", ', '.join[lettres_envoyees]) #affiche les lettres essayees
          
                #dmd une lettre a l'utilisateur 
            lettre = input("Proposez une lettre:").upper() #conveetit en majuscule

                #verif lettre ou autre
            if len(lettre) != 1 or not lettre.isalpha(): #isalpha verifie si cest bien une lettre et non un chiffre ou symbole
                print("Veuillez entrer une seule lettre.")
                continue 

                    # verif lettre deja proposer ou non 
            if lettre in lettres_envoyees: 
                print("Vous avez déja essayé cette lettre.")
                continue
                    #ajt la letrre a la liste des lettres qui sont éssayés
            lettres_envoyees.append(lettre) 

                # verif si la lettre est dans les mots a deviner
            if lettre in mot_a_deviner:
                lettres_trouvees.append(lettre) #ajt la lettre aux lettres trouvées 
                print("Bonne lettre!")
            else: 
                essais_restants-=1 #diminue le nombre de tentaties restantes   
                print("Mauvaises lettres!") 
                
            print(dessinPendu(6 - essais_restants)) #maj du pendu 
            