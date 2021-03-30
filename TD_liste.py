#Exercice 3

    
t = []
for i in range(0,10,2):
    t.append(i**2)
    
    
   
#Exercice 4

t = [0]*10

for i in range(len(t)):
    t[i] = 10 - i
    


# Exercice 5
liste_nom=['Jean-Michel','Marc','Vanessa','Anne','Maximilien','Alexandre-Benoît','Louise']

def longueurNomV1(liste_nom):
    liste_longueur = []
    for nom in liste_nom:
        liste_longueur.append(len(nom))
    return liste_longueur

def longueurNomV2(liste_nom):
    liste_longueur = [0]*len(liste_nom)
    for i in range(len(liste_nom)):
        liste_longueur[i] = len(liste_nom[i])
    return liste_longueur


#Exercice 6
t=['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']

def affiche_liste(list):
    phrase = " "
    for mot in len(list):
        phrase += list[mot]
    print(phrase)


        