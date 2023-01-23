#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:54:51 2023

@author: 21214576
"""

def Gs(liste_proposition, liste_reponse, capacite):
    Etat_proposition = []
    proposition_arret = []
    Etat_reponse = []
    res = []
    for i in range(len(liste_proposition)):
        Etat_proposition.append(0)
        proposition_arret.append(0)
        
    for i in range(len(liste_reponse)):
        Etat_reponse.append(0)
        
    is_end = False
        
    while(not is_end):
        is_find = False
        choix = -1
        index = 0
        while(not is_find):
            if(Etat_proposition[index] == 0):
                is_find = True
                choix = index
            if (index == len(liste_proposition) - 1):
                is_end = True
            index += 1
        if (not (choix == -1)):
            for i in range(proposition_arret[choix], len(liste_reponse)):
                proposition_arret[choix] += 1
                if (Etat_reponse[liste_proposition[choix][i]] < capacite[liste_proposition[choix][i]]):
                    liste_temp = [choix, liste_proposition[choix][i]]
                    res.append(liste_temp)
                    Etat_proposition[choix] = 1
                    Etat_reponse[liste_proposition[choix][i]] += 1
                    break
                else:
                    last_proposition = find_last(res, liste_proposition[choix][i])
                    if (inferieur(choix, last_proposition, liste_reponse[liste_proposition[choix][i]])):
                        Etat_proposition[res[last_proposition][0]] = 0
                        del res[last_proposition]
                        liste_temp = [choix, liste_proposition[choix][i]]
                        Etat_proposition[choix] = 1
                        res.append(liste_temp)
                        break
    return res
                
def find_last(liste, val):
    last_position = -1
    for i in range(len(liste)):
        if(liste[i][1] == val):
            last_position = i
    
    return last_position

def inferieur(x, y, liste):
    return liste.index(x) < liste.index(y)
    
    
        
