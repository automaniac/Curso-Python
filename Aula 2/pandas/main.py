import pandas as pd

# dataframe = pd.read_csv('pnt.csv')

# print(dataframe.head())

# print('informacoes:')
# print(dataframe.info())
# print('Estatisticas do dado:')
# print(dataframe.describe())

# fluxo = dataframe['Flow'].tolist()

# print(fluxo)

data = {'nome': ['Alice', 'Bob', 'Charlie', 'Dave'],
        'idade': [25, 30, 35, 40]}

df_data = pd.DataFrame(data)

# print(df_data.head())

# def incrementar_idade(idade):
#     return idade +1

# dataframe_novo = df_data['idade'].map(incrementar_idade)
# print(dataframe_novo)

# dataframe_novo.to_csv('teste.csv')
print(df_data.iloc[2])





