from tictactoe.board import Board
from tictactoe.ui import ConsoleUI

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.joueur = "Joueur 1"
        self.tours = 0
        self.board = Board()
        self.console = ConsoleUI(self.board)

    def jeu(self):
        while True:
            self.tours += 1
            self.console.afficher_message(f"\nTour #{self.tours}\n")
            self.board.afficher_grille()
            ligne, colonne = self.console.demander_position(self.joueur)
            self.board.placer_un_symbole(self.joueur, ligne, colonne)
            if self.board.verifier_victoire():
                self.console.afficher_message("\n")
                self.board.afficher_grille()
                self.console.afficher_message(f"\n{self.joueur} a gagné la partie")
                break
            if self.board.verifier_egalite():
                self.board.afficher_grille()
                self.console.afficher_message(f"\nLa partie est nulle!")
                break
            self.joueur = "Joueur 2" if self.joueur == "Joueur 1" else "Joueur 1"
        self.restart()
        

    def restart(self):
        while True:
            recommencer = self.console.recommencer()
            if recommencer:
                self.reset()
                self.jeu()
                break
            else:
                self.console.afficher_message("\nMerci d'avoir joue!")
                break
