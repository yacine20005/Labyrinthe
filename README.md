# Labyrinthe

## Description du jeu

Labyrinthe est un jeu où vous incarnez un aventurier explorant un donjon rempli de dragons. Votre objectif est de trouver et vaincre les dragons tout en naviguant à travers un labyrinthe de salles rotatives.

## Objectif du jeu

L'objectif principal du jeu est de trouver et vaincre tous les dragons présents dans le donjon. Pour ce faire, vous devez naviguer à travers le labyrinthe, en utilisant les salles rotatives pour créer des chemins et accéder aux dragons.

## Comment jouer

1. Lancez le jeu en suivant les instructions d'installation et d'exécution ci-dessous.
2. Utilisez les touches de direction pour déplacer votre aventurier à travers le labyrinthe.
3. Utilisez la barre d'espace pour faire pivoter les salles et créer de nouveaux chemins.
4. Trouvez et vainquez tous les dragons pour gagner la partie.

## Installation et exécution

### Prérequis

- Python 3.x
- Bibliothèque `fltk`

### Instructions

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/yacine20005/Labyrinthe.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd Labyrinthe
   ```
3. Exécutez le jeu :
   ```bash
   python main.py
   ```

## Contrôles et mécaniques du jeu

- Utilisez les touches de direction pour déplacer votre aventurier.
- Appuyez sur la barre d'espace pour faire pivoter les salles.
- Les salles rotatives peuvent être utilisées pour créer de nouveaux chemins et accéder aux dragons.

## Structure du jeu

Le jeu est composé de plusieurs éléments principaux :

- **Menu principal** : Permet de lancer une nouvelle partie ou d'accéder aux options.
- **Menu des options** : Permet de choisir la carte et les paramètres de jeu.
- **Plateau de jeu** : Représenté sous forme de grille avec différentes tuiles représentant les salles du donjon.
- **Aventurier** : Personnage contrôlé par le joueur, représenté par une image sur le plateau de jeu.
- **Dragons** : Ennemis à vaincre, représentés par des images sur le plateau de jeu.

## Cartes du jeu

Le jeu inclut plusieurs cartes stockées dans le répertoire `ressources/maps`. Chaque carte est représentée par un fichier texte contenant la disposition des salles et les positions des dragons.

### Ajouter une nouvelle carte

Pour ajouter une nouvelle carte, suivez ces étapes :

1. Créez un nouveau fichier texte dans le répertoire `ressources/maps`.
2. Définissez la disposition des salles en utilisant les caractères appropriés (voir `ressources/tiles.txt` pour les symboles disponibles).
3. Ajoutez les positions de l'aventurier et des dragons à la fin du fichier, en utilisant le format suivant :
   ```
   A x y
   D x y niveau
   ```
   Où `x` et `y` sont les coordonnées de la position, et `niveau` est le niveau du dragon.
