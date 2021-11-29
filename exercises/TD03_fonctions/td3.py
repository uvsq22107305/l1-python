#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    
    return temps[0]*24*3600 + temps [1]*3600 + temps[2]*60 + temps [3]

mon_temps = (3,23,1,34)
print(type(mon_temps))
print(tempsEnSeconde((9, 54, 34, 6))) 

b= tempsEnSeconde(mon_temps)

print (b)   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour= seconde // 86400 
    seconde = seconde % 86400

    heure  = seconde // 3600
    seconde = seconde % 3600

    minutes = seconde // 60
    seconde = seconde % 60
    return  (jour, heure, minutes, seconde)

t = 234342352

print (secondeEnTemps(t))


#fonction auxiliaire ici
def affichagepluriel(val,mot) :
   if val != 0 :
        print (" ",val, mot, end = "")   
   if val > 1 :
        print("s", end = "")    

     

def afficheTemps(temps):
    affichagepluriel(temps[0], "jour")
    affichagepluriel(temps[1], "heure")
    affichagepluriel(temps[2], "minute")
    affichagepluriel(temps[3],"seconde")
    print()
    

    
afficheTemps((2,1,14,23)) 

def demandeTemps():
    jour = int((input("Entrée le nombre de jour")))
    
    heures = int((input("Entrée le nombre d'heures")))

    while heures >  23 and  heures >= 0 :
        heures = int((input("Entrée le nombre d'heures")))

    minutes = int((input("Entrée le nombre de minutes")))
    
    while minutes > 59 and  minutes >= 0 :
        minutes = int((input("Entrée le nombre d'heures")))

    secondes = int((input("Entrée le nombre de secondes")))
    
    while secondes > 59 and  secondes >= 0 :
        secondes = int((input("Entrée le nombre d'heures")))


    return (jour, heures, minutes, secondes )


afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    
   
    temps = (temps1[0]+ temps2[0],temps1[1]+ temps2[1],temps1[2]+ temps2[2],temps1[3]+ temps2[3])

    return (temps)

    
temps1 = (2,3,4,25)
temps2 = (5,22,57,1)

print(sommeTemps(temps1, temps2))

def proportionTemps(temps,proportion):
   
    b =  tempsEnSeconde(temps)  

    c= int (b * proportion)

    d= secondeEnTemps(c)

    return d

temps = (2,0,36,0)
proportion = 0.2



print(afficheTemps(proportionTemps(temps,proportion)))


