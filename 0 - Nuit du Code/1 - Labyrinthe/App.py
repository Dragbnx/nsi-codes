import pyxel
from Personnage import *
from Labyrinthe import *
BLOC = 8
HAUT, BAS, GAUCHE, DROITE = (0, -BLOC), (0, BLOC), (-BLOC, 0), (BLOC, 0)


class App:
    """ Application graphique - Pyxel """
    def __init__(self):
        """ App -> None """
        # initialisation de la fenêtre graphique
        self.hero = Personnage(8,8)
        self.commandes = {pyxel.KEY_RIGHT: DROITE,
                          pyxel.KEY_UP: HAUT,
                          pyxel.KEY_LEFT: GAUCHE,
                          pyxel.KEY_DOWN: BAS,
                          };
        self.lab = Labyrinthe(51,51)
        pyxel.init(408, 408, title="La Nuit du Code")
        pyxel.init(128, 128, title="La Nuit du Code")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ App -> None
        Met à jour l'application """

    def draw(self):
        """ App -> None
        Affiche les éléments dans la fenêtre graphique """

    
    
    def deplacer(self, perso, direction):
        """ App, Personnage, (int, int) -> None
        Déplace le personnage dans la direction indiquée si cela est possible """
        xp, yp = self.hero.x//BLOC, self.hero.y//BLOC
        x, y = direction
        x, y = x//8, y//8
        if self.lab.est_sol((x+xp,y+yp)):
            self.hero.x += x*8
            self.hero.y += y*8





        pass

App()