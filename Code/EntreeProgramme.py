import FichierAListe # Pour pouvoir utiliser les methodes de exemple.py
import AlgoGS

#print("bonjour")
ListeEtu = FichierAListe.lectureFichier("PrefEtu.txt") # Execution de la methode lectureFichier du fichier exemple.
ListeParcour, capacite = FichierAListe.lectureFichierSpe("PrefSpe.txt")

#print(ListeEtu)
#print(ListeParcour)

print(AlgoGS.Gs(ListeEtu, ListeParcour, capacite))




"""
print(maListe)
print(len(maListe)) #Longueur de la liste.
exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier
"""
