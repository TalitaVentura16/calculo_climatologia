import pandas as pd

# Ler arquivo Excel
amazonia = '/home/talita/Documentos/calculo_climatologia/calculo_python/pentada_amazonia_atualizada.xlsx'

# Transformar em dataframe
df = pd.read_excel(amazonia)

# Remover a última coluna (Pentada) para o cálculo da média
df_num = df.drop(columns=["Pentada"])

# Calcular a média das colunas numéricas
df["Media"] = df_num.mean(axis=1)

# Inicializar lista para armazenar resultados
inicio_seca = []

# Pegar todas as colunas de anos, exceto 'Pentada' e 'Media'
anos = df.columns[1:-1]

# Loop pelas pentadas de 8 em 8 para cada ano
for ano in anos:
    for i in range(len(df) - 7):
        pentada_atual = df.iloc[i]
        pentadas_seguintes = df.iloc[i+1:i+8]
        
        abaixo_da_media = pentadas_seguintes[pentadas_seguintes[ano] < pentadas_seguintes["Media"]]
        
        if len(abaixo_da_media) >= 6:
            num_pentada = pentadas_seguintes["Pentada"].values[0]  # Obtém o número da primeira pentada
            inicio_seca.append(f'Ano: {ano}, Pentada: {num_pentada} - Início da estação seca')

# Imprime o resultado
if inicio_seca:
    for frase in inicio_seca:
        print(frase)
else:
    print("Erro ao processar a base")
