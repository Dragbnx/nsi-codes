def code_ascii(texte):
    """ str -> [int]
    Renvoie la liste des codes ascii des caractères du texte """
    return [ord(c) for c in texte]

def decode_ascii(codes):
    """ [int] -> str
    Renvoie la chaîne de caractères correspondant aux codes ascii """
    return "".join([chr(c) for c in codes])

def genere_alphabet_majuscule():
    """ () -> [str]
    Renvoie la liste des 26 lettres de l'alphabet latin en majuscule """
    return [chr(c)
            for c in range(ord('A'), ord('Z') + 1)]
    # return  [chr(ord('A') + c) for c in range(26)]

def decale_car(car, cle):
    """ str, int -> str
    Si car est une majuscule,
    renvoie le caractère correspondant à car, décalé de cle """
    if not ord('A') <= ord(car) <= ord('Z'):
        return car
    res = ord(car) # un nombre entre 65 et 90
    res = res - ord('A') # un nombre entre 0 et 25
    res = (res + cle)%26 # un nombre entre 0 et 25
    res = res + ord('A')
    return chr(res)
    

def chiffre_cesar(clair, cle):
    """ str, int -> str
    Chiffre le clair avec le chiffrement de César (cle = décalage) """
    return "".join([decale_car(c, cle) for c in clair])
    # chiffre = ""
    # for car in clair:
    #     chiffre += decale_car(car, cle)
    # return chiffre

def dechiffre_cesar(chiffre, cle):
    """ str, int -> str
    Renvoie le texte clair vérifiant chiffre = chiffre_cesar(clair, cle) """
    return chiffre_cesar(chiffre, -cle)

# la valeur de la clé est la même pour chiffrer
# ou déchiffrer : c'est un chiffrement symétrique

# Texte de l'énigme
chiffre = """
OH 28 DYULO 1942, D ZDVKLQJWRQ G.F.

D TXL GH GURLW.
PD GHFRXYHUWH SRUWH VXU OD VWUXFWXUH GH OD PDFKLQH HQLJPD. HOOH SHUPHW GH IDLUH GHV VXFFHVVLRQV GH VXEVWLWXWLRQV HW GH SHUPXWDWLRQV. M'DL DXVVL O'LPSUHVVLRQ TXH OD VWUXFWXUH GHV PHVVDJHV HFKDQJHV HVW VRXYHQW OD PHPH, FH TXH QRXV DOORQV WHQWHU G'HASORLWHU.

HOLCDEHWK VPLWK IULHGPDQ.
SRVW-VFULSWXP : SRUWHC FH YLHXA ZLVNB DX MXJH EORQG TXL IXPH. 
"""

# on suppose que "OH" correspond à "LE"
# on devine le décalage = 3
# car de E à H : 3 lettres

# Texte déchiffré
# dechiffre_cesar(chiffre, 3)

def indice_lettre(c):
    """ str -> int
    Renvoie l'indice dans l'alphabet de la lettre capitale c. """
    return ord(c) - ord('A')

cle = [indice_lettre(c) for c in "NSI"]
print(cle)


def chiffre_vigenere(clair, cle):
    """ str, [int] -> str
    Chiffrement de Vigenère """
    chiffre = []
    compteur = 0
    m = len(clair)
    n = len(cle)
    cle = cle*((m//n)+1)
    for c in clair:
        chiffre.append(chiffre_cesar(c,cle[compteur]))
        compteur+=1
    return "".join(chiffre)

# À retenir :
# différence entre codage et chiffrement :
# codage = référence commune, partagée, publique
# (exemple : ASCII, Morse, unicode)
# chiffrement = se base sur une clé secrète.
# des méthodes pour chiffer et déchiffrer :
# on a besoin de :
# - une méthode de chiffrement
# - une clé qui est partagée : on utilise
# la même clé pour le chiffrement et le
# déchiffrement (fonctionnement symétrique).
# Une personne qui ne connait pas la clé ne
# peut pas
# - chiffrer un message
# - déchiffrer le message









