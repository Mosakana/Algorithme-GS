#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:22:48 2023

@author: 21214576
"""

def inferieur(x, y, liste):
    return liste.index(x) < liste.index(y)

def find_member(liste_result, parcour):
    liste_temp = []
    for i in range(len(liste_result)):
        if liste_result[i][1] == parcour:
            liste_temp.append(liste_result[i][0])
            
    return liste_temp


def find_instable(result, liste_reponse, liste_proposititon):
    liste_instable = []
    for i in range(len(result)):
        stop_point = liste_reponse.index(result[i][1])
        for j in range(stop_point):
            parcour_test = liste_reponse[j]
            liste_member = find_member(result, parcour_test)
            for s in range(len(liste_member)):
                if inferieur(result[i][0], liste_member[s], liste_proposititon[parcour_test]):
                    liste_instable.append([result[i][0], parcour_test])
    
    return list_instable
                
            
            
