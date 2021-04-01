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
#Exercice 7
    
def enleveDoublon(list_int):
    list_element = []
    for i in list_int:
        if i not in list_element:
            list_element.append(i)
    return list_element

# Exercice 8


def alterne(liste1,liste2):
    new_list = []
    
    for i in range(len(liste1)):
        new_list.append(liste1[i])
        new_list.append(liste2[i])
        
    return new_list
liste1=['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre'] 
liste2=[31,28,31,30,31,30,31,31,30,31,30,31]        
        
            

##def alterne2(liste1,liste2):
##    new_list = [0]*len(liste1)*2
##    
##    for i in range(len(liste1)):
##        new_list[i] = liste1[i]
##        new_list[i+1] = liste2[i]
##        
##        
##    return new_list

# Exercice 9
def trouve_le_meme(l1,l2):
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            print(i,l1[i])
b=[9093,2559,9664,8075,4525,5847,67,8932,5049,5241,5886,1393,9413,8872,2560,4636,9004,7586,1461,350,2627,2187,7778,8933,351,7097,356,4110,1393,4864,1088,3904,5623,8040,7273,1114,4394,4108,7123,8001,5715,7215,7460,5829,9513,1256,4052,1585,1608,3941]
a=[8468,4560,3941,3328,7,9910,9208,8400,6502,1076,5921,6720,948,9561,7391,7745,9007,9707,4370,9636,5265,2638,8919,7814,5142,1060,6971,4065,4629,4490,2480,9180,5623,6600,1764,9846,7605,8271,4681,2818,832,5280,3170,8965,4332,3198,9454,2025,2373,4067]



#Exercice 10

def permute(liste,i,j):
    """description: échange dans la liste les éléments d'indice i et jliste (list)i, j (int): indices des éléments à permuter
 ATTENTION : MODIFICATION DE LA LISTE EN PLACE !!"""
    x = i
    i = j
    liste.append(liste[i])
    liste.append(liste[x])
liste=["Bob","Alice","Marc","Tom","John"]
