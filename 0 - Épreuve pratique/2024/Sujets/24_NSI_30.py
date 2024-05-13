def fusion(l1, l2):
    pile = Pile()
    while not est_vide(l1) and not est_vide(l2):
        if tete(l1) > tete(l2):
            pile.empiler(tete(l2))
            l2 = queue(l2)
        else :
            pile.empiler(tete(l1))
            l1 = queue(l1)
    l = creer_vide()
    while not pile.est_vide():
        l = ajoute(l, pile.depiler())
    return l

def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre] 
    elif romains[nombre[0]] >= romains[nombre[1]]: 
        return romains[nombre[0]] + traduire_romain(nombre[1:]) 
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]] 
    

