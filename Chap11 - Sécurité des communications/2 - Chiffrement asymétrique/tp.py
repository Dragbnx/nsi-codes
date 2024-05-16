import random

def nombres_premiers(n):
    """ int -> [int]
    Renvoie la liste des nombres premiers inférieurs ou égaux à n """
    pass

def diviseurs_premiers(n):
    """ int -> {int}
    Renvoie l'ensemble des diviseurs de n """
    pass

def premiers_entre_eux(a, b):
    """ int, int -> bool
    Renvoie True si et seulement si a et b sont premiers entre eux """
    pass

def inverse_modulo(n, a):
    """ int, int -> int
    Renvoie (si possible) l'inverse de a modulo n """
    pass

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

