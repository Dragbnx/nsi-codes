import pyxel

BLOC = 8
HAUT, BAS, GAUCHE, DROITE = (0, -BLOC), (0, BLOC), (-BLOC, 0), (BLOC, 0)


class Personnage:
    """Un personnage dans le labyrinthe"""

    def __init__(self, x=0, y=0):
        """ Personnage -> None """
        self.x = x
        self.y = y
    def deplacer(self, direction):
        """ Personnage, (int, int) -> None
        Met à jour la position du personnage après un
        déplacement de direction = (dx, dy) """
        x, y = direction
        self.x += x
        self.y += y

    def haut(self):
        self.deplacer(HAUT)

    def bas(self):
        self.deplacer(BAS)

    def gauche(self):
        self.deplacer(GAUCHE)

    def droite(self):
        self.deplacer(DROITE)

    def afficher(self, couleur=5):
        """ Personnage -> None
        Affiche le personnage à l'écran """
        pyxel.rect(self.x, self.y, 8, 8, couleur)