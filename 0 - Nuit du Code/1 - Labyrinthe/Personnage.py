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
        pass
    
    def afficher(self):
        """ Personnage -> None
        Affiche le personnage à l'écran """
        pass
