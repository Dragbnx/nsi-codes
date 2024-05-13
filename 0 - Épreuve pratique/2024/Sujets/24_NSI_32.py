def ou_exclusif(tab1, tab2):
    """
    Renvoie un tableau où chaque élément est le résultat de l'opérateur
    "ou exclusif" entre les éléments correspondants des deux tableaux passés en paramètres.
    """
    if len(tab1) != len(tab2):
        return "Les tableaux n'ont pas la même longueur."

    resultat = []

    for i in range(len(tab1)):
        resultat.append(tab1[i] ^ tab2[i])

    return resultat



class Carre:
    def __init__(self, liste, n): 
        self.ordre = n        
        self.tableau = [[liste[i + j * n] for i in range(n)] 
                        for j in range(n)] 
                                   
    def affiche(self):        
        '''Affiche un carré''' 
        for i in range(self.ordre): 
            print(self.tableau[i]) 
                                   
    def somme_ligne(self, i): 
        '''Calcule la somme des valeurs de la ligne i''' 
        somme = 0             
                                   
        for j in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
    def somme_col(self, j):   
        '''Calcule la somme des valeurs de la colonne j''' 
        somme = 0
                                   
        for i in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
                                   
    def est_semimagique(self): 
        s = self.somme_ligne(0)
        for i in range(1, self.ordre):
            if self.somme_ligne(i) != s:
                return False
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False
        return True


lst_c2 = [2, 7, 6, 9]
c2 = Carre(lst_c2, 2)

lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
c3 = Carre(lst_c3, 3)



print(c2.est_semimagique())    
print(c3.est_semimagique())    


