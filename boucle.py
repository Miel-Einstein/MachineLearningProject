i=1
while i<=7:
    print(i)
    if i==3:
       print('nous sommes a trois') 
    i=i+1

#continue  saute cette valeur , break(pause) arrete toi ici

voitures=['tesla','ferrari','porsche']
for i in voitures:
    if i=="ferrari":
        print('ferrari is more expensive')
        continue 
    print(i)

# dictionnaire
# pdict={'smart':100,'iphone':500,'motorola':10}
# for key ,value in pdict.items():
    
#     if value==500:
#        print('500 c est hyper chere') 
#        continue
#     print(key)
#     print(value,'euro')
       
for i in range(6,-6,-1):  
     if i==0:
       print(i, "nous sommes a l'origine") 
       continue
     print(i)

voitures=['tesla','ferrari','porsche']
caParjour=[1000,15000,19999]

for i in range(len(voitures)):
    print(voitures[i],caParjour[i])

def calculerPttc(pht,ptva):
    pttc=pht*(1+ptva)
    return pttc

print('le prix pttc est = ',calculerPttc(10,4))

    