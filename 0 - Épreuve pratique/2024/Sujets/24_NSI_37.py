def moyenne(tab):
    if len(tab) == 0:
        return 0
    total = 0
    for num in tab:
        total += num
    return total/len(tab)


def tri(tab):
    i = 0
    j = len(tab) - 1
    while i <= j :
        if tab[i]==0:
            i += 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i]= valeur
            j -=1
David
