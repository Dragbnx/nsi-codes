def max_et_indice(tab):
    if tab==[]:
        return None

    max_element = tab[0]  
    max_indice = 0          

    for i in range(1, len(tab)):
        if tab[i] > max_element:
            max_element = tab[i] 
            max_indice = i          

    return max_element, max_index







    def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    vus = [False] * n
    for v in tab:
        if v < 1 or v > n or vus[v-1]:
            return False
        vus[v-1] = True
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de points de rupture de ordre qui représente 
    un ordre de gènes de chromosome.
    '''
    # Vérification que ordre est un ordre de gènes
    assert est_un_ordre(ordre)
    
    n = len(ordre)
    nb = 0
    if ordre[0] != 1:
        nb += 1
    i = 0
    while i < n - 1: 
        diff = ordre[i] - ordre[i+1]  
        if diff != 1 and diff != -1: 
            nb += 1
        i += 1
    if ordre[-1] != n: 
        nb += 1
    return nb


