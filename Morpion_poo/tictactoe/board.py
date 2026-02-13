
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