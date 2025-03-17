# Jeu du Pendu  

## Description  
Ce projet est une version simple du jeu du Pendu en Python. Le but est de deviner un mot en proposant des lettres une par une. À chaque erreur, une partie du pendu est dessinée. Le jeu s’arrête quand le mot est trouvé ou quand le dessin est complet.  

## Fonctionnalités  
- Choix aléatoire d’un mot à deviner  
- Affichage du mot sous forme masquée (`* * * *`)  
- Nombre d’essais limités  
- Affichage progressif du pendu  

## Comment jouer ?  
1. **Cloner le dépôt** :  
   ```sh
   git clone https://github.com/TonNomGitHub/NomDuRepo.git
   cd NomDuRepo
   ```  
2. **Lancer le programme** :  
   ```sh
   python pendu.py
   ```  
3. **Règles du jeu** :  
   ° Un mot caché est affiché sous forme de tirets.  
   - Le joueur propose une lettre.  
   - Si la lettre est correcte, elle apparaît dans le mot.  
   - Sinon, une partie du pendu est ajoutée.  
   - La partie se termine quand le mot est trouvé ou quand le pendu est complété.  
