import random

def nombres_premiers(n):
    """ int -> [int]
    Renvoie la liste des nombres premiers inférieurs ou égaux à n """
    if n <= 1:
        return []
    l = [True]*(n+1)
    l[0], l[1] = False, False
    for i in range(2, n):
        if not l[i]:
            continue
        for j in range(2*i, n+1, i):
            l[j] = False
    rep = [i for i in range(len(l)) if l[i]]
    return rep

def diviseurs_premiers(n):
    """ int -> {int}
    Renvoie l'ensemble des diviseurs de n """
    diviseurs_poss = nombres_premiers(n)
    divisieurs_premiers = set()
    for elm in diviseurs_poss:
        if n%elm == 0:
            divisieurs_premiers.add(elm)
    return divisieurs_premiers


def premiers_entre_eux(a, b):
    """ int, int -> bool
    Renvoie True si et seulement si a et b sont premiers entre eux """
    diviseur_a = diviseurs_premiers(a)
    diviseur_b = diviseurs_premiers(b)
    for elm in diviseur_a:
        if elm in diviseur_b:
            return False
    return True


def inverse_modulo(n, a):
    """ int, int -> int
    Renvoie (si possible) l'inverse de a modulo n """
    for i in range(n)
        if (a*i%n) == 1:
            return i

def decompose(n):
    """ int -> {int:int}
    Décompose n en produit de facteurs premiers """
    pass

def genere_RSA(p, q):
    """ int, int -> (int, int), (int, int)
    Génère un couple de clé privée/clé publique pour RSA """
    pass

def chiffre_RSA(M, pk):
    """ int, (int, int) -> int
    Chiffre le message M à l'aide de la clé publique """
    n, e = pk
    # À compléter

def dechiffre_RSA(C, sk):
    """ int, (int, int)
    Déchiffre le message chiffré C à l'aide de la clé secrète """
    pass

def chiffre_texte_RSA(clair, pk):
    """ str, (int, int) -> [int]
    Chiffre le texte à l'aide du chiffrement RSA et de la clé publique pk """
    pass

def dechiffre_texte_RSA(chiffre, sk):
    """ [int], (int, int) -> str
    Déchiffre le message chiffre """
    pass

def chiffre_texte_RSA_blocs(clair, pk):
    """ str, (int, int) -> [int]
    Chiffre le texte clair à l'aide d'un chiffrement RSA par bloc """
    pass

def dechiffre_texte_RSA_blocs(chiffre, sk):
    """ [int], (int, int) -> str
    Déchiffre le message chiffre à l'aide d'un chiffrement RSA par blocs """
    pass

