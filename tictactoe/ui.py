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
