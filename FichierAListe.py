def lectureFichier(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne
    res = []
    length = int(contenu[0])
    del contenu[0]
    for i in range(length):
        contenu[i] = contenu[i].split()
        liste = []
        for j in range(9):
            liste.append(int(contenu[i][j + 2]))
        res.append(liste)
                
         
    monFichier.close() #Fermeture du fichier
    #contenu[0]=contenu[0].split()     # ligne.split() renvoie une liste de toutes les chaines contenues dans la chaine ligne (separateur=espace)
    #contenu[1]=contenu[1].split()
    return res
    # Commandes utiles:
    # n=int(s) transforme la chaine s en entier.
    # s=str(n) l'inverse
    # Quelques methodes sur les listes:
    # l.append(t) ajoute t a la fin de la liste l
    # l.index(t) renvoie la position de t dans l (s'assurer que t est dans l)
    # for s in l: s vaut successivement chacun des elements de l (pas les indices, les elements)
    
def lectureFichierSpe(s):
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne
    res = []
    capacite = []
    contenu[1] = contenu[1].split()
    for e in range (1, 10):
        capacite.append(int(contenu[1][e]))
    
    del contenu[0]
    del contenu[0]
    
    for i in range(9):
        contenu[i] = contenu[i].split()
        liste = []
        for j in range(11):
            liste.append(int(contenu[i][j + 2]))
        res.append(liste)
    
    monFichier.close()
    
    return res, capacite
    


def createFichierLP(nomFichier,nombreVariables):
    monFichier=open(nomFichier,"w") #Ouverture en ecriture. Le fichier est ecrase s'il existe, cree s'il n'existe pas
    monFichier.write("Maximize\n")
    for i in range(0,nombreVariables): #Boucle i variant de 0 a NombreVariables-1
        monFichier.write("x"+str(i)+" ") #write pour ecrire. Indentation
        if (i<nombreVariables-1): # Syntaxe d'un test. 'and' et 'or' dans les expressions logique
            monFichier.write("+ ")
        else:
            monFichier.write("\n")
    monFichier.write("st\n") # Fin de l'indentation -> fin de la boucle
    monFichier.write("Binary\n")
    for i in range(0,nombreVariables):
        monFichier.write("x"+str(i)+" ")
    monFichier.write("\n")
    monFichier.write("end")
    monFichier.close()
