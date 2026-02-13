# la_map# # . . .
# # . . .
# # . . .
# valeur_nulle = ' . '
# valeur_1 = ' O '
# valeur_2 = ' X '

# # La map du morpion
# la_map = [
#     [valeur_nulle, valeur_nulle, valeur_nulle],
#     [valeur_nulle, valeur_nulle, valeur_nulle],
#     [valeur_nulle, valeur_nulle, valeur_nulle]
# ]

# joueur_en_cours = "Joueur 1" 

# # Fonction pour dessiner la map
# def draw(): 
#     for i in range(3):
#         for j in range(3):
#             print(la_map[i][j], end="")
#         print()

# # Fonction qui explore toutes les possibilité pour quil y ait un gagnant 
# def check_win():
#     # Vérifier si nous n'avons pas le même symbole sur les lignes
#     for i in range(3):
#         if la_map[i][0] == la_map[i][1] == la_map[i][2] != valeur_nulle :
#             return True
        
#     # Vérifier si nous n'avons pas le même symbole sur les colonnes 
#     for j in range(3):
#         if la_map[0][j] == la_map[1][j] == la_map[2][j] != valeur_nulle:
#             return True
    
#     # Vérifier les diagonales 
#     if la_map[0][0] == la_map[1][1] == la_map[2][2] != valeur_nulle :
#         return True
#     if la_map[0][2] == la_map[1][1] == la_map[2][0] != valeur_nulle :
#         return True

# # Vérifier qu'il ne reste plus de point vide
# def check_map(): 
#     for i in range(3):
#         for j in range(3):
#             if la_map[i][j] == valeur_nulle:
#                 return False
#     return True

# # Premier dessin de la map
# draw()

# # Lancement du jeu
# while True: 
#     # Demander au joueur d'entrer son choix 
#     # Vérifier la matrice 
#     # Si un jour gagne ou la partie est égale on fait un break
#     entree = int(input(f"{joueur_en_cours} [1-9] ? > "))

#     ligne = (entree - 1) // 3 # 2
#     colonne = (entree - 1) % 3 # 0

#     if la_map[ligne][colonne] == valeur_nulle:
#         la_map[ligne][colonne] = valeur_1 if joueur_en_cours == 'Joueur 1' else valeur_2

#     draw()
#     print(entree)

#     # Vérifier s'il y a un gagnant
#     if check_win():
#         print(f"{joueur_en_cours} a gagné ! ")
#         break

#     # Vérifier si la partie est nulle
#     if check_map():
#         print("Match nul !")
#         break
    
#     # Si personne ne gagne, vérifier si la map n'est pas pleine
#     # Si la map est pleine, c'est match nul

#     joueur_en_cours = "Joueur 1" if joueur_en_cours == "Joueur 2" else "Joueur 2"


# # Ajouter la logique qui permet à un joueur de recommancer si son entrée est déjà prise, ou est invalide (entree qui n'est pas entre le 1 et le 9)





#----------------------------------------------------------------------------
class Board:
    valeur_nulle = ' . '
    valeur_1 = ' O '
    valeur_2 = ' X '
    
    def __init__(self):
        self.creer_grille()

    def creer_grille(self):
        self.grille = [
[self.valeur_nulle, self.valeur_nulle, self.valeur_nulle],
[self.valeur_nulle, self.valeur_nulle, self.valeur_nulle],
[self.valeur_nulle, self.valeur_nulle, self.valeur_nulle]
]
    def afficher_grille(self):
        for i in range(3):
            for j in range(3):
                print(self.grille[i][j], end="")
            print()

    def placer_un_symbole(self, joueur, ligne, colonne):
        self.grille[ligne][colonne] = Board.valeur_1 if joueur == "Joueur 1" else Board.valeur_2
        

    def verifier_victoire(self):
    # Vérifier si nous n'avons pas le même symbole sur les colonnes 
        for j in range(3):
            if self.grille[0][j] == self.grille[1][j] == self.grille[2][j] != Board.valeur_nulle:
                return True
        
        # Vérifier si nous n'avons pas le même symbole sur les lignes
        for i in range(3):
            if self.grille[i][0] == self.grille[i][1] == self.grille[i][2] != Board.valeur_nulle :
                return True


        # Vérifier les diagonales 
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != Board.valeur_nulle :
            return True
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != Board.valeur_nulle :
            return True
        return False


    def verifier_egalite(self):
            # Vérifier si nous n'avons pas le même symbole sur les lignes
        for ligne in self.grille:
            if self.valeur_nulle in ligne:
                return False
        return True


#----------------------------------------------------------------------------


class Game:
    def __init__(self):
        self.joueur = "Joueur 1"
        self.tours = 0
        self.board = Board()
        self.console = ConsoleUI(self.board)

    def jeu(self):
        while True:
            self.tours += 1
            print(f"Tour #{self.tours}")
            self.board.afficher_grille()
            ligne, colonne = self.console.demander_position(self.joueur)
            self.board.placer_un_symbole(self.joueur, ligne, colonne)
            if self.board.verifier_victoire():
                self.board.afficher_grille()
                self.console.afficher_message(f"{self.joueur} a gagné la partie")
                break
            if self.board.verifier_egalite():
                self.board.afficher_grille()
                self.console.afficher_message(f"La partie est nulle!")
                break
            self.joueur = "Joueur 2" if self.joueur == "Joueur 1" else "Joueur 1"
        


#----------------------------------------------------------------------------

class ConsoleUI:
    
    def __init__(self, board):
        self.board = board


    def demander_position(self, joueur):
        while True:
            try:
                position = int(input(f"{joueur} [1-9] ? > "))
            except ValueError:
                print("Erreur: Veuillez entrer un nombre entier entre 1 et 9")
                continue
            if not 1 <= position <= 9:
                print("Erreur: Veuillez entrer un nombre entre 1 et 9")
                continue
            ligne = (position - 1) // 3 # 2
            colonne = (position - 1) % 3 # 0
            if self.board.grille[ligne][colonne] == self.board.valeur_nulle:
                return ligne, colonne
            else:
                print(f"Cette case est deja occupee par {self.board.grille[ligne][colonne]}")

    def afficher_message(self, message):
        print(f"{message}")

def main():
    partie = Game()
    partie.jeu()

main()