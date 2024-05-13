def recherche_min(tab):
    if not tab:
        return None
    min = 0
    for i in range(1,len(tab)):
        if tab[i]<tab[min]:
            min = i
    return min

def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab) - 1 
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = gauche + 1 
        else :
            tab[gauche] = tab[droite]
            tab[droite] = tab[gauche]
            droite = droite - 1
    return tab


