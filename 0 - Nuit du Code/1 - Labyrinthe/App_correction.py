import pyxel
import random

BLOC = 8
HAUT, BAS, GAUCHE, DROITE = (0, -BLOC), (0, BLOC), (-BLOC, 0), (BLOC, 0)

class App:
    """Application graphique - Pyxel"""
    def __init__(self):
        """App -> None"""
        pyxel.init(128, 128, fps = 10, title="La Nuit du Code")
        pyxel.load("1.pyxres")
        self.heros = Personnage(8, 8)
        self.win = False
        self.lab = Labyrinthe(15, 15)
        # # commandes[touche] = action
        # self.commandes = {
        #     pyxel.KEY_RIGHT: self.heros.droite,
        #     pyxel.KEY_UP: self.heros.haut,
        #     pyxel.KEY_LEFT: self.heros.gauche,
        #     pyxel.KEY_DOWN: self.heros.bas
        # }       
        self.commandes = {
            pyxel.KEY_RIGHT: lambda: self.deplacer(self.heros, DROITE),
            pyxel.KEY_UP: lambda: self.deplacer(self.heros, HAUT),
            pyxel.KEY_LEFT: lambda: self.deplacer(self.heros, GAUCHE),
            pyxel.KEY_DOWN: lambda: self.deplacer(self.heros, BAS)
        }       
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """ App -> None
        Met à jour l'application """
        self.exec_btn()
        
    
    def draw(self):
        """ App -> None
        Affiche les éléments dans la fenêtre graphique """
        pyxel.cls(0)
        self.lab.afficher()
        self.heros.afficher()
        if self.win:
            pyxel.text(50, 50, "YOU WIN", 0)

    def exec_btn(self):
        """ App -> None
        Exécute toutes les commandes correspondant
        aux boutons actuellement pressés """
        # pour chacunes des touches connectées à des commandes :
        # on vérifie si la touche est pressée.
        # Si c'est le cas, on exécute la commande correspondante.
        for k in self.commandes:
            if pyxel.btn(k):
                self.commandes[k]()
    
    def deplacer(self, perso, direction):
        """ App, Personnage, (int, int) -> None
        Déplace le personnage perso dans la direction indiquée si cela est possible """
        dx, dy = direction
        i, j = (perso.x + dx)//BLOC, (perso.y + dy)//BLOC
        if self.lab.est_sol((i, j)):
            perso.deplacer(direction)
        if self.lab.est_fin((i, j)):
            self.win = True

class Personnage:
    """Un personnage dans le labyrinthe"""
    def __init__(self, x=0, y=0):
        """Personnage -> None"""
        self.x = x
        self.y = y
        self.textures = [(i, 16) for i in range(0, 24, 8)]

    def deplacer(self, direction):
        """ Personnage, (int, int) -> None
        Met à jour la position du personnage après un
        déplacement de direction = (dx, dy) """
        dx, dy = direction
        self.x += dx
        self.y += dy
    
    def afficher(self, couleur=5):
        """ Personnage -> None
        Affiche le personnage à l'écran """
        # Comment faire pour :
        # Ralentir l'animation ?
        # Accélerer l'animation ?
        # Changer le personnage : oiseau -> blob vert
        # "Intégrer" le personnage au labyrinthe
        # (la couleur violette doit apparaître comme transparente)
        u, v = self.textures[pyxel.frame_count%len(self.textures)]
        pyxel.blt(self.x, self.y, 0, u, v, BLOC, BLOC)
        # pyxel.rect( BLOC, BLOC, couleur)
    
    def haut(self): self.deplacer(HAUT)
    def bas(self): self.deplacer(BAS)
    def droite(self): self.deplacer(DROITE)
    def gauche(self): self.deplacer(GAUCHE)

class Labyrinthe:
    """Représente un labyrinthe"""
    def __init__(self, n, m):
        """Labyrinthe, int, int -> None
        Initialise un labyrinthe vide """
        assert n%2 == 1 and m%2 == 1
        self.dim = n, m
        self.murs = [[0 for j in range(m)]
                    for i in range(n)]
        self.sortie = (13, 13)
        self.textures = {
            0: (0, 40),
            1: (40, 0)
        }
        self.generer()
        # self.murs = self.creer_lab_fusion(n, m)

    def est_dans(self, position):
        """ Labyrinthe, (int, int) -> bool
        Détermine si position est un indice de bloc valide pour le labyrinthe self """
        i, j = position
        n, m = self.dim
        return 0 <= i < n and 0 <= j < m
    
    def est_sol(self, position):
        """ Labyrinthe, (int, int) -> bool
        Détermine si position est un indice de bloc valide pour le labyrinthe self """
        i, j = position
        return self.est_dans(position) and self.murs[i][j] == 0

    def est_fin(self, position):
        return position == self.sortie
    
    def blocs_possibles(self, position, visites):
        """ Labyrinthe, (int, int), {(int, int)} -> [(int, int)]
        Renvoie la liste des blocs voisins et non visités """
        i, j = position
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        voisins = []
        for di, dj in directions:
            nouvelle_position = i + 2*di, j + 2*dj
            if self.est_dans(nouvelle_position) and not nouvelle_position in visites:
                voisins.append(nouvelle_position)
        return voisins
    
    def generer(self):
        """ Labyrinthe -> None
        Génère un labyrinthe de manière aléatoire """
        n, m = self.dim
        # Initialement tous les murs sont fermés
        # et aucun bloc  n'a été visité
        for i in range(n):
            for j in range(m):
                if not (i%2 == 1 and j%2 == 1):
                    self.murs[i][j] = 1
        visites = set()
        chemin = []
        # on marque le bloc comme étant visité
        position_courante = (1, 1)
        visites.add(position_courante)
        chemin.append(position_courante)
        while chemin:
            position_courante = chemin[-1]
            voisins = self.blocs_possibles(position_courante, visites)
            if voisins:
                nouvelle_position = random.choice(voisins)
                i = (position_courante[0] + nouvelle_position[0])//2
                j = (position_courante[1] + nouvelle_position[1])//2
                self.murs[i][j] = 0
                visites.add(nouvelle_position)
                chemin.append(nouvelle_position)
                position_courante = nouvelle_position
            else:
                chemin.pop()

    def creer_lab_fusion(self, n, m):
        mat = [[ int((j - 1)/2 + (i - 1)/2*m) if i%2 == 1 and j%2 == 1 else 1
                 for j in range(2*m + 1)]
                 for i in range(2*n + 1)]
        aretes = { (i, j)
                   for i in range(1, 2*n)
                   for j in range(1, 2*m)
                   if (i%2 == 1) ^ (j%2 == 1) }
        while len(aretes) > 0:
            # Choix d'une arête aléatoire
            i, j = random.sample(aretes, 1)[0]
            aretes.remove((i, j))
            # arête verticale 
            if i%2 == 1 and not mat[i][j + 1] == mat[i][j - 1]:
                mat[i][j] = 0 # on ouvre le mur à l'arête choisie
                old_num, new_num = mat[i][j + 1], mat[i][j - 1]
                self.propage(mat, i, j + 1, old_num, new_num)
            # arête verticale 
            elif j % 2 == 1 and not mat[i + 1][j] == mat[i - 1][j]:
                mat[i][j] = 0 # on ouvre le mur à l'arête choisie
                old_num, new_num = mat[i + 1][j], mat[i - 1][j]
                self.propage(mat, i + 1, j, old_num, new_num)
        # nettoyage si necessaire : les cases de sol = 0, les cases de mur = -1
        if mat[1][1] != 0:
            self.propage(mat, 1, 1, mat[1][1], 0)
        for row in mat:
            print("".join([str(c).rjust(4) for c in row]))
        return mat

    def propage(self, mat, i, j, old_num, new_num):
        N, M = len(mat), len(mat[0])
        directions = (1, 0), (0, -1), (-1, 0), (0, 1)
        mat[i][j] = new_num
        for dx, dy in directions:
            new_i, new_j = i + 2*dx, j + 2*dy
            if 0 <= new_i < N and 0 <= new_j < M and mat[new_i][new_j] == old_num:
                self.propage(mat, new_i, new_j, old_num, new_num)
    
    def afficher(self):
        """ Labyrinthe -> None
        Affiche le labyrinthe self à l'écran """
        n, m = self.dim
        for i in range(0, n):
            for j in range(0, m):
                u, v = self.textures[self.murs[i][j]]
                # Comment faire pour changer le thème ?
                pyxel.blt(i*BLOC, j*BLOC, 0, u, v, BLOC, BLOC)
                # pyxel.rect(i*BLOC, j*BLOC, h, w, col)

App()
