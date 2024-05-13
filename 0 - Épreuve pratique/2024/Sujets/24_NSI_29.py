#maximilien ILIC
def moyennes(n):
    denominateur = 0
    numerateur = 0
    for i in range(len(n)):
        denominateur += n[i][1]
        numerateur += n[i][0] * n[i][1]
    return numerateur/denominateur


def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1] 
    for i in range(1, len(ligne)): 
        ligne_suiv.append(ligne[i]+ligne[i-1]) 
    ligne_suiv.append(1) 
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n): 
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle
