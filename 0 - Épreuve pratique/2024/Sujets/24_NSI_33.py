# Sujet n°33
# Exercice 1

def renverse(mot):
    inverse = ""
    for c in mot:
        inverse = c + inverse
    return inverse
    

# Exercice 2

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers += [i]
            multiple  = i + i
            while multiple < n:
                tab[multiple] = False
                multiple = multiple + i
    return premiers
    

