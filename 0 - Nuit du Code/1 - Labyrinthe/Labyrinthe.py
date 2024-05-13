class Labyrinthe:
    """Représente un labyrinthe"""
    def __init__(self, n, m):
        """Labyrinthe, int, int -> None
        Initialise un labyrinthe vide """
        assert n%2 == 1 and m%2 == 1
        self.dim = n, m
        self.murs = [[0 for j in range(m)]
                    for i in range(n)]

    def est_dans(self, bloc):
        """ Labyrinthe, (int, int) -> bool
        Détermine si bloc est un indice de bloc valide pour le labyrinthe self """
        pass
    
    def est_sol(self, bloc):
        """ Labyrinthe, (int, int) -> bool
        Détermine si bloc est un indice de bloc valide correspondant à un sol dans le labyrinthe self """

        x,y = bloc
        return self.murs[x][y] != 0

        pass

    
    def blocs_possibles(self, position, visites):
        """ Labyrinthe, (int, int), {(int, int)} -> [(int, int)]
        Renvoie la liste des blocs voisins et non visités """
        pass
    
    def generer(self, couleur = 1):
        """ Labyrinthe
        Génère un labyrinthe de manière aléatoire """

        n, m = self.dim
        for i in range(n):
            for j in range(m):
                if i%2 == 1 and j%2 == 1:
                    self.murs[i][j] = couleur
        visites = set()
        chemin = []
        position_courantes = (1,1)
        visites.add(position_courantes)
        chemin.append(position_courantes)
        while chemin != []:
            choix = self.blocs_possibles(position_courantes, visites)
            if choix == []:
                chemin.pop()
                if chemin!= []:
                    position_courantes = chemin[-1]
                continue
            nouvelle_position = random.choice(choix)
            x, y = position_courantes
            x1, y1 = nouvelle_position
            self.murs[(x+x1)//2][(y+y1)//2] = couleur
            position_courantes = nouvelle_position
            visites.add(position_courantes)
            chemin.append(position_courantes)

    def afficher(self):
        """ Labyrinthe -> None
        Affiche le labyrinthe self à l'écran """
        n,m = self.dim
        for i in range(n):
            for j in range(m):
                pyxel.rect(i*8, j*8, 8, 8, self.murs[i][j])

Labyrinthe(15,15)
        pass
    
    def afficher(self):
        """ Labyrinthe -> None
        Affiche le labyrinthe self à l'écran """
        pass
