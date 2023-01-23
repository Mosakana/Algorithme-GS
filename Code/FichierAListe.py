nombreEtu = 11
nombreSpe = 9

def lectureFichierEtu(s):  # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r")  # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines()  # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne
    res = []
    dictEtu = dict()
    del contenu[0]
    for i in range(nombreEtu):
        contenu[i] = contenu[i].split()
        liste = []

        dictEtu[int(contenu[i][0])] = contenu[i][1]
        for j in range(nombreSpe):
            liste.append(int(contenu[i][j + 2]))
        res.append(liste)

    monFichier.close()  # Fermeture du fichier
    # contenu[0]=contenu[0].split()     # ligne.split() renvoie une liste de toutes les chaines contenues dans la chaine ligne (separateur=espace)
    # contenu[1]=contenu[1].split()
    return res, dictEtu
    # Commandes utiles:
    # n=int(s) transforme la chaine s en entier.
    # s=str(n) l'inverse
    # Quelques methodes sur les listes:
    # l.append(t) ajoute t a la fin de la liste l
    # l.index(t) renvoie la position de t dans l (s'assurer que t est dans l)
    # for s in l: s vaut successivement chacun des elements de l (pas les indices, les elements)


def lectureFichierSpe(s):
    monFichier = open(s, "r")  # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines()  # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne
    res = []
    capacite = []
    dictSpe = dict()
    contenu[1] = contenu[1].split()
    del contenu[1][0]
    for e in range(nombreSpe):
        capacite.append(int(contenu[1][e]))

    del contenu[0]
    del contenu[0]

    for i in range(nombreSpe):
        contenu[i] = contenu[i].split()
        liste = []

        dictSpe[int(contenu[i][0])] = contenu[i][1]
        for j in range(nombreEtu):
            liste.append(int(contenu[i][j + 2]))
        res.append(liste)

    monFichier.close()

    return res, capacite, dictSpe


def createFichierLP(nomFichier, nombreVariables):
    monFichier = open(nomFichier,
                      "w")  # Ouverture en ecriture. Le fichier est ecrase s'il existe, cree s'il n'existe pas
    monFichier.write("Maximize\n")
    for i in range(0, nombreVariables):  # Boucle i variant de 0 a NombreVariables-1
        monFichier.write("x" + str(i) + " ")  # write pour ecrire. Indentation
        if (i < nombreVariables - 1):  # Syntaxe d'un test. 'and' et 'or' dans les expressions logique
            monFichier.write("+ ")
        else:
            monFichier.write("\n")
    monFichier.write("st\n")  # Fin de l'indentation -> fin de la boucle
    monFichier.write("Binary\n")
    for i in range(0, nombreVariables):
        monFichier.write("x" + str(i) + " ")
    monFichier.write("\n")
    monFichier.write("end")
    monFichier.close()
