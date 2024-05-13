def recherche_motif(motif, texte):
    l=[]
    for i in range(len(texte)-len(motif)+1):
        j = 0
        while j < len(motif) and motif[j] == texte[i+j]:
            j += 1
        if j == len(motif):
            l.append(i)
    return l

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)
            
def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc
