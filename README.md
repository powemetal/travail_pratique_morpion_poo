Auteurs:  
-Francis Boisvert
-Lilia Ould Hocine (code de base du morpion) https://github.com/liliaouldhocine

Ce projet a été réalisé dans le cadre d’un exercice du cours Concepts de programmation 1, dans le programme d’Attestation d’études collégiales (AEC) en développement de logiciels du Collège de Maisonneuve.


# ÉNONCÉ 2 — Morpion version POO (Programmation Orientée Objet)

## Objectif

Vous devez créer une version du morpion utilisant la **programmation orientée objet (POO)** et un **package Python**. https://github.com/liliaouldhocine/a25-cdp1/blob/main/semaine5/jeu-morpion.py

Ce travail vous permettra de comprendre :

- comment créer des classes
- comment organiser un projet POO
- comment séparer les responsabilités dans différentes classes

---

## Structure obligatoire

```
morpion_poo/
│
├── main.py
│
└── tictactoe/
    ├── __init__.py
    ├── board.py
    ├── game.py
    └── ui.py
```

---

## Classes obligatoires

Vous devez créer les classes suivantes :

---

### Classe Board (board.py)

Responsabilités :

- créer la grille
- afficher la grille
- placer un symbole
- vérifier victoire
- vérifier égalité

---

### Classe Game (game.py)

Responsabilités :

- gérer le joueur courant
- gérer les tours
- gérer la boucle du jeu
- détecter la fin de partie

---

### Classe ConsoleUI (ui.py)

Responsabilités :

- demander une position
- afficher des messages

---

### main.py

Responsabilités :

- créer les objets
- démarrer le jeu

---

## Exemple de fonctionnement attendu

```
 .  .  .
 .  .  .
 .  .  .

Joueur 1 [1-9] ? > 1
 .  .  .
 .  .  .
 O  .  .

Joueur 2 [1-9] ? > 5
```

---

## Contraintes obligatoires

Vous devez utiliser :

- au moins 2 classes
- au moins 2 fichiers contenant des classes
- un package Python
- des imports corrects

Exemple :

```python
from tictactoe.game import Game
```

---

## Critères de réussite

Votre projet doit :

- fonctionner correctement
- utiliser la POO
- utiliser un package
- utiliser plusieurs modules
- avoir un code structuré

---

## Bonus (optionnel)

Ajouter :

- une méthode restart()
- un compteur de tours
- afficher le gagnant avec un message spécial