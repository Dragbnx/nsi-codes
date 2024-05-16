# attention à la lecture de l'énoncé :
# def liste_puissances_borne(a,n,borne=None):
def liste_puissances_borne(a,borne):
        def puissance(a,n):
            result = 1
            for _ in range(n):
                    result *= a
            return result
        # borne n'est pas jamais None, c'est un paramètre de la fonction
        # if borne is None:
        # return [puissance(a,i) for i in range(i,borne) if abs(puissance(a,i)) < abs(borne)]
        return [puissance(a,i) for i in range(1,borne) if puissance(a,i) < borne]

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

# La fonction est incorrecte :  elle ne vérifie pas les exemples de l'énoncé.
def codes_parfait(mot):
    """Renvoie un triplet 
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""
    code_concatene = ""
    code_additionne = 0 
    for c in mot:
        code_concatene = code_concatene + str(ord(c))
        code_additionne = code_additionne +  ord(c)
    code_concatene = int(code_concatene)
    # Par ailleurs, on dit que ce mot est « parfait » si le code additionné divise le code concaténé
    # la ligne suivante est donc incorrecte
    mot_est_parfait = (len(set(mot)) == len(mot))
    return code_additionne, code_concatene, mot_est_parfait


