from numpy import NaN
from analyzecsv import *
# People number

numb_p=len(nam)
print("il y'a" ,numb_p,"personnes dans ce bateau")
#Male and Female number
men=sex.count('male')
women=sex.count('female')
print("il y'a" ,men,"hommes et ",women," femmes dans ce bateau")
#pourcent of Survived
survivant=surv.count(1)
non_survivant=surv.count(0)
print("il y'a" ,survivant,"  survivants et ",non_survivant,"non survivant")
pourcentage_survi=survivant/len(surv)
print("le pourcentage de survi est de ",pourcentage_survi)

#l'age moyen des personnes 

print(ag)
print("l'age moyen des personnes dans le bateau etait de",sum(ag)/len(ag))

nom='Astor, Col. John Jacob'
ind=nam.index(nom)
for i in nam:
    if i==nom:
       print(nom,f'se trouve evidemment dans le bateau at the index {ind}') 
       break

print('Astor, Col. John Jacob' in nam)

print(nam.pop(43))
nam.insert(43,'miel einstein')
print(nam.pop(43))