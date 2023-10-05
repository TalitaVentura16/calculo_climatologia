# Este programa tem como objetivo calcular o cumprimento da estacao seca e o inicio da estacao chuvosa 
# 

import pandas as pd

# Ler arquivo em excel
amazonia = 'pentada_amazonia_atualizada.xlsx'

# Transformar em dataframe 
df = pd.read_excel(amazonia)

# calcular media
df["Media"] = df.iloc[:, :-1].mean(axis=1)

# Loop pelas pentadas de 8 em 8 para cada ano
inicio_seca = []
anos = df.columns[:-2]  # Pega todas as colunas de anos, exceto a coluna "Pentada" e "Media"

for ano in anos:
    for i in range(1, len(df), 8):
        pentadas = df.iloc[i:i+8]
        coluna_ano = ano
        coluna_media = "Media"
        abaixo_da_media = pentadas[(pentadas[coluna_ano] < pentadas[coluna_media])]
        if len(abaixo_da_media) >= 6:
            num_pentada = pentadas["Pentada"].values[0]  # Obtém o número da pentada da primeira linha
            inicio_seca.append(f'Ano: {ano}, Pentada: {num_pentada} - Início da estação seca')

# Imprime o resultado
for frase in inicio_seca:
    print(frase)

# Se nada for encontrado, imprime "Erro ao processar a base"
if not inicio_seca:
    print("Erro ao processar a base")



