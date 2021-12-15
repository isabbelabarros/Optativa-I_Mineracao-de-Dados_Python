import pandas as pd
import matplotlib.pyplot as plt

#Isabela Maria Barros
#Matrícula: 16-95950

df = pd.read_csv('titanic.csv',sep=",")

#Letra A
print(df.head(10))

#Letra B
df.sort_values('Name',inplace=True)
print(df.head(2))

#Letra C
df['Sobrevivente'] = df['Survived']
df['Sobrevivente'] = df['Sobrevivente'].replace([0],'Não')
df['Sobrevivente'] = df['Sobrevivente'].replace([1],'Sim')
df.sort_values(by=['Name'],inplace=True)
print(df.head(2))

#Letra D:
df.drop('SibSp',axis=1,inplace=True)
df.drop('Parch',axis=1,inplace=True)
df.drop('Ticket',axis=1,inplace=True)
print(df.head(2))

#Letra E
df.rename(columns={'PassengerID': 'IDPassageiro','Survived': 'Sobreviveram','Pclass': 'Pclasse','Name': 'Nome','Sex':'Sexo','Age':'Idade','Fare':'Tarifa','Cabin':'Cabine','Embarked':'Embarcou'},inplace=True)
print(df.head(2))

#Letra F
df['Sexo'] = df['Sexo'].map({'male':'masculino','female':'FEMININO'},na_action=None)
print(df.head(5))

#Letra G
df['Sobreviveram'].fillna(0,inplace=True)
df.drop(df.loc[df['Sobreviveram'] == 0].index,inplace=True)
sobreviventesGroup = df.groupby('Pclasse',as_index = False)['Sobreviveram'].sum()
print(sobreviventesGroup)

#Letra H
df['Sobreviveram'].fillna(1,inplace=True)
df.drop(df.loc[df['Sobreviveram'] == 1].index,inplace=True)
mortosGroup = df.groupby('Sexo',as_index = False)['Sobreviveram'].count()
print(mortosGroup)

#Letra I
plt.bar(sobreviventesGroup['Pclasse'],sobreviventesGroup['Sobreviveram'])
plt.title('Sobrevivente por classe')
plt.xlabel('Classe')
plt.ylabel('Sobreviventes')
plt.show()

#Letra J
dfExcel = pd.ExcelWriter('titanic.xlsx')
df.to_excel(dfExcel,index=False)
dfExcel.save()
