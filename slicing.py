import numpy as np 
import pandas as pd

#le slicing indiquer queller serie de valeur on souhaite selectionner

pays=np.array([['Congo','Cameroun','Gabon'],
[1000,500,100],[2021,2020,5],[7,8,9]
])
print(pays[0,0]) # le prmier pour la ligne , le deuxieme c'est pour selectionner la colonne
print(pays[:,1])
print(pays[2:3,:])

pays=pays[1:]
print(pays)
pays=pays.astype(int)
# print(pays)
# print(pays[2,0]-1)
# print(pays**2)

a=np.array([2,5,20])
b=np.array([4,5,22])
a[2]=14
# print(a)
c=np.concatenate((a,b)) #  in np.concatenate double the parenthesis
print(c)
#np.nan dire que la valeur n'existe pas pour eviter des erreures de calcules
np.nan_to_num(pays) # remplace la valeur nan par 0

pays1=np.array([[3,4],
               [5,6]
               ])
pays2=np.array([[1,2]
        ,[5,9]])

# print(pays1+pays2)

pays3=np.concatenate((pays1,pays2))
# print(pays3)

# for i in np.arange(0,11,1):
#     if i==5: 
#         print(i,"* 3 = ",3*i,"ici c la moitie")
#         continue
#     # print(i,"* 3 = ",3*i)

#     np.linspace(6,100,13) # le 13 ici est mis pour l'ecart graphique surtout

produitsDict={
    'Smartphone':{'prix':111,'enStock':True},
    'Compas':{'prix':2,'enStock':False}
}
# print(produitsDict)
df=pd.DataFrame(produitsDict)
print(pays)
df2=pd.DataFrame(pays, columns=['Congo','Italie','France'])
print(df2)
data=pd.read_csv('tested.csv',encoding='latin-1',sep=",")
print(data.head(2))
print(data.info())
print(data.dtypes)
print(data.shape)
print('voici le premier ' ,data.iloc[0,0])
data2=pd.read_csv('metal.csv',encoding="latin-1",sep=",")
print(data2.head())

print(data2.iloc[0:3,0:5])

print(df.loc[['prix','enStock'],['Compas']])

print(data2.loc[1:3,['band_name','formed']])

for row_index,row in data2.head(5).iterrows():
    print(row_index,row['split'])