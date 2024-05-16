from Personnage import *
from Labyrinthe import *
import time
import pyxel
BLOC = 8
HAUT, BAS, GAUCHE, DROITE = (0, -BLOC), (0, BLOC), (-BLOC, 0), (BLOC, 0)


class App:
    """ Application graphique - Pyxel """

    def __init__(self, w, h):
        """ App -> None """
        # initialisation de la fenêtre graphique
        self.w, self.h = w, h
        self.lab = Labyrinthe(w//8,h//8)
        self.hero = Personnage(5,8, 8)
        sol = self.lab.liste_sol()
        sol = random.choice(sol)
        x,y = sol
        self.monstre = Personnage(8, x*8, y*8)
        self.commandes = {pyxel.KEY_RIGHT: DROITE,
                          pyxel.KEY_UP: HAUT,
                          pyxel.KEY_LEFT: GAUCHE,
                          pyxel.KEY_DOWN: BAS,
                          };
        self.fin = False
        pyxel.init(w, h, title="La Nuit du Code", fps = 40)
        pyxel.run(self.update, self.draw)
        #NE RIEN METTRE APRES !!! CONNARD!!!


    def exec_btn(self):
        for cle in self.commandes:
            if pyxel.btn(cle):
                self.deplacer(self.hero, self.commandes[cle])


    def ennemi(self):
        choix = random.choice([HAUT, BAS, GAUCHE, DROITE])
        self.deplacer(self.monstre, choix)

    def update(self):
        """ App -> None
        Met à jour l'application """
        self.exec_btn()
        self.ennemi()
        bloc = self.hero.x//8, self.hero.y//8
        if self.lab.arrive(bloc):
            self.fin = True



    def draw(self):
        """ App -> None
        Affiche les éléments dans la fenêtre graphique """
        pyxel.cls(0)
        self.lab.afficher()
        self.hero.afficher()
        self.monstre.afficher()
        if self.fin:
            pyxel.cls(0)
            pyxel.text(self.w/2, self.h/2, 'WIN', 7)

    def deplacer(self, perso, direction):
        """ App, Personnage, (int, int) -> None
        Déplace le personnage dans la direction indiquée si cela est possible """
        xp, yp = perso.x//BLOC, perso.y//BLOC
        x, y = direction
        x, y = x//8, y//8
        if self.lab.est_sol((x+xp,y+yp)):
            perso.x += x*8
            perso.y += y*8






App( 264, 264)