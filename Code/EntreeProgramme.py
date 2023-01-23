import FichierAListe  # Pour pouvoir utiliser les methodes de exemple.py
import AlgoGS

# print("bonjour")
ListeEtu, dictEtu = FichierAListe.lectureFichierEtu(
    "..//Resource//PrefEtu.txt")  # Execution de la methode lectureFichier du fichier exemple.
ListeParcour, capacite, dictSpe = FichierAListe.lectureFichierSpe("..//Resource//PrefSpe.txt")

# print(ListeEtu)
# print(ListeParcour)

resultat = AlgoGS.GsEtu(ListeEtu, ListeParcour, capacite)
for element in resultat:
    print("({Etu}, {Parcours})".format(Etu = dictEtu[element[0]], Parcours = dictSpe[element[1]]))

"""
print(maListe)
print(len(maListe)) #Longueur de la liste.
exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier
"""
