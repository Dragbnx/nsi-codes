def code_ascii(texte):
    """ str -> [int]
    Renvoie la liste des codes ascii des caractères du texte """
    return [ord(elm) for elm in texte]


def decode_ascii(codes):
    """ [int] -> str
    Renvoie la chaîne de caractères correspondant aux codes ascii """
    return "".join([chr(elm) for elm in codes])


def genere_alphabet_majuscule():
    """ () -> [str]
    Renvoie la liste des 26 lettres de l'alphabet latin en majuscule """
    return [chr(elm) for elm in range(65, 91)]

def decale_car(car, cle):
    """ str, int -> str
    Si car est une majuscule,
    renvoie le caractère correspondant à car, décalé de cle """
    if not ord('A') <= ord(car) <= ord('Z'):
        return car
    res = ((ord(car) - 65) + cle)%26 + ord('A')
    return chr(res)


def chiffre_cesar(clair, cle):
    """ str, int -> str
    Chiffre le clair avec le chiffrement de César (cle = décalage) """
    return ''.join([decale_car(car, cle) for car in clair])

def dechiffre_cesar(chiffre, cle):
    """ str, int -> str
    Renvoie le texte clair vérifiant chiffre = chiffre_cesar(clair, cle) """
    return chiffre_cesar(chiffre, 26-cle)


def brute_force_cesar(chiffre):
    for i in range(1,26):
        print(f'{dechiffre_cesar(chiffre, i)}, cle = {i}')




def indices_lettres(c):
    return ord(c)-ord('A')



def chiffre_vigenere(clair, cle):
    """ str, [int] -> str
    Chiffrement de Vigenère """
    new = ''
    for i in range(len(clair)):
        new += chiffre_cesar(clair[i], cle[i%len(cle)])
    return new

cle = [indices_lettres(c) for c in 'NSI']
print(cle)
print(chiffre_vigenere("TENEZ BON", cle))