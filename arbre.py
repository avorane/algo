#!/usr/bin/env python


class Noeud(object):

    def __init__(self, value=None):
        self.value = value
        self.noeud_gauche = None
        self.noeud_droit = None
        
    def inserer_noeud(self, noeud):
        if noeud.value < self.value: 
            if self.noeud_gauche is None:
                self.noeud_gauche = noeud
            else:
                self.noeud_gauche.inserer_noeud(noeud)
        else:
            if self.noeud_droit is None:
                self.noeud_droit = noeud
            else:
                self.noeud_droit.inserer_noeud(noeud)
                
class Arbre(object):

    def __init__(self):
        self.racine = None
        
    def inserer_noeud(self, value):
        noeud = Noeud(value)
        if self.racine is None:
            self.racine = noeud
        else:
            self.racine.inserer_noeud(noeud)
            

if __name__ == "__main__":
    noeuds = [21, 12, 78, 52, 47, 10, 89, 52, 63]
    arbre = Arbre()
    for noeud in noeuds:
        arbre.inserer_noeud(noeud)
    
