def recherches_indices_classement(elt, tab):
    moins, egal, sup = [], [], []
    for i in range(len(tab)):
        if tab[i] == elt:
            egal.append(i)
        elif tab[i] < elt:
            moins.append(i)
        else:
            sup.append(i)
    return moins, egal, sup

resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
    },
    'Durand': {
        'DS1': [6 , 4],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [12, 4]
    }
}

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
    resultats. Si nom n'est pas dans le dictionnaire, 
    la fonction renvoie None.'''
    if nom in resultats:
        notes = resultats[nom]
        if not notes:
            return 0
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points += note * coefficient
            total_coefficients += coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return None


