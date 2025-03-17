# Jeu du Pendu  

## Description  
Ce projet est une implémentation du jeu du Pendu en Python. L'objectif est de deviner un mot en proposant des lettres une par une. Chaque erreur rapproche du dessin complet du pendu. Le jeu se termine si le mot est trouvé ou si le pendu est entièrement dessiné.  

## Fonctionnalités  
- Sélection aléatoire d’un mot à deviner  
- Affichage du mot sous forme masquée (`* * * *`)  
- Gestion des essais limités et affichage du pendu étape par étape  
- Mode console simple et interactif  

## Comment jouer ?  
1. **Cloner le dépôt** sur ton ordinateur :  
   ```sh
   git clone https://github.com/TonNomGitHub/NomDuRepo.git
   cd NomDuRepo
   ```  
2. **Lancer le jeu** avec Python :  
   ```sh
   python pendu.py
   ```  
3. **Règles** :  
   - Une série de `* * * *` représente le mot à deviner.  
   - Propose une lettre au clavier.  
   - Si la lettre est correcte, elle s'affiche dans le mot.  
   - Si la lettre est incorrecte, une partie du pendu apparaît.  
   - Tu gagnes en trouvant le mot avant d'atteindre le nombre maximal d’erreurs.  
