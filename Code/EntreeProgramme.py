import FichierAListe  # Pour pouvoir utiliser les methodes de exemple.py
import AlgoGS

# print("bonjour")
ListeEtu, dictEtu = FichierAListe.lectureFichierEtu(
    "..//Resource//PrefEtu.txt")  # Execution de la methode lectureFichier du fichier exemple.
ListeParcour, capacite, dictSpe = FichierAListe.lectureFichierSpe("..//Resource//PrefSpe.txt")

# print(ListeEtu)
# print(ListeParcour)

def find_member(liste_result, parcour):
    liste_temp = []
    for i in range(len(liste_result)):
        if liste_result[i][1] == parcour:
            liste_temp.append(liste_result[i][0])
            
    return liste_temp

def inferieur(x, y, liste):
    return liste.index(x) < liste.index(y)


def find_instable(result, liste_proposition, liste_reponse):
    liste_instable = []
    for i in range(len(result)):
        stop_point = liste_proposition[i].index(result[i][1])
        for j in range(stop_point):
            parcour_test = liste_proposition[i][j]
            liste_member = find_member(result, parcour_test)
            for s in range(len(liste_member)):
                if inferieur(result[i][0], liste_member[s], liste_reponse[parcour_test]):
                    liste_instable.append([result[i][0], parcour_test])
    
    return liste_instable
                


resultat = AlgoGS.GsEtu(ListeEtu, ListeParcour, capacite)
#resultat = [[0, 5], [1, 6], [4, 1], [5, 0], [3, 0], [7, 7], [9, 2], [6, 8], [10, 4], [8, 8], [2, 3]] 
liste_instable = find_instable(resultat, ListeEtu, ListeParcour)
print(liste_instable)
for element in resultat:
    #print("({Etu}, {Parcours})".format(Etu = dictEtu[element[0]], Parcours = dictSpe[element[1]]))
    print("({Etu}, {Parcours})".format(Etu = element[0], Parcours = element[1]))

"""
print(maListe)
print(len(maListe)) #Longueur de la liste.
exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier
"""


