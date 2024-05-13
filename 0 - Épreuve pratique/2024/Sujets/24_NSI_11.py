# EXERCICE 1

def nombre_de_mots(phrase):
    mots = 0
    espaces = 0
    exclamation_ou_interrogation = 0
    for mot in phrase:
        if mot == " ":
            espaces += 1
        if mot == "?" or mot == "!":
            exclamation_ou_interrogation +=1
    mots = (espaces + 1) - exclamation_ou_interrogation
    return mots
    
    
print("   EXERCICE 1   ")
print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est séparé !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))







# EXERCICE 2

class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit != None:
                self.droit = inserer(cle)
            else:
                self.droit = Noeud(cle)
                
                
print("   EXERCICE 2   ")

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
print(arbre.gauche.etiquette)
print(arbre.droit.etiquette)
print(arbre.gauche.gauche.etiquette)
print(arbre.gauche.droit.etiquette)



