def multiplication(n1, n2): # Exercice 1
    resultat = 0
    if n1<0 and n2<0 or n1<0:
        n1 = -n1
        n2 = -n2
    for i in range(n1):
        resultat += n2
    return resultat

def chercher(tab, x, i, j): # Exercice 2
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x: 
        return chercher(tab, x, m , j) 
    elif tab[m] > x:
        return chercher(tab, x, i , m) 
    else:
        return m