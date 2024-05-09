## programa inicial

import pandas as pd

def detecta_inicio_seca(arquivo_excel):
    # Ler o DataFrame a partir do arquivo Excel
    df = pd.read_excel(arquivo_excel)

    # Calcular a média
    df["Media"] = df.iloc[:, :-1].mean(axis=1)

    # Inicializar uma lista para armazenar as detecções de início de estação seca
    inicio_seca = []

    # Definir o número de linhas que você deseja comparar (8 no seu caso)
    num_linhas_comparacao = 8

    # Percorrer as linhas do DataFrame (exceto as 8 últimas linhas, uma vez que você precisa de 8 linhas para comparação)
    for i in range(len(df) - num_linhas_comparacao):
        # Inicializar um contador para contar quantos valores estão abaixo da média
        count_abaixo_da_media = 0

        # Percorrer as colunas dos anos
        for ano in df.columns[:-2]:
            # Comparar o valor da coluna do ano com o valor da coluna de média para a linha atual e as 7 seguintes
            if all(df[ano].iloc[i:i+num_linhas_comparacao] < df['Media'].iloc[i:i+num_linhas_comparacao]):
                count_abaixo_da_media += 1

        # Verificar se pelo menos 6 dos 8 valores estão abaixo da média
        if count_abaixo_da_media >= 6:
            # Se a condição for atendida, registrar o início da estação seca
            inicio_seca.append(f'Pentada: {i+1} - Início da estação seca')

    return inicio_seca

resultado = detecta_inicio_seca('pentada_amazonia_atualizada.xlsx')

# Verificar se algo foi encontrado
if resultado:
    # Imprimir as detecções de início de estação seca
    for frase in resultado:
        print(frase)
else:
    # Imprimir mensagem de erro
    print("Não foi detectado o início da estação seca para a base informada.")
