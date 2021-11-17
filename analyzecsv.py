import pandas as pd 
# analyze titanic
df=pd.read_csv('tested.csv',sep=',')
df=df.dropna()
print(df)
surv=df['Survived'].tolist()
nam=df['Name'].tolist()
sex=df['Sex'].tolist()
ag=df['Age'].tolist()

print('Survived:',surv)
print('Name :',nam)
print('Sexe:',sex)
print('age:',ag)


# liste=[list(x) for x in df.values]
# for i in liste:
#    print(i)

