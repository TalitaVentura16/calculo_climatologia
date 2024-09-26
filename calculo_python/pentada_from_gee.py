# O objetivo deste programa eh coletar dados de precipitacao em uma regiao definida, 
# a fim de se construir uma base de dados que registre a acumulacao de chuva em intervalos
# de 5 dias, durante um periodo continuo de 305 dias. Na terminologia climatologica, esses 
# intervalos sao referidos como "pentadas".

# importacao do google earth engine
import ee
import pandas as pd
from datetime import datetime, timedelta

def calcula_pentada(dataInicio, dataFim):
    # Autenticação e inicialização da API
    ee.Authenticate()
    ee.Initialize()

    # Base utilizada para a coleta de dados
    dataset = ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD') \
        .filterDate(dataInicio, dataFim)

    # Selecionar a banda de precipitacao
    precipitation = dataset.select('precipitation')

    # Inicializar variaveis para rastrear o ano e a numeração da pentada
    ano_atual = None
    num_pentada = 0

    # Crie um dicionario para armazenar os valores de precipitacao por ano
    valores_por_ano = {}

    
    # Percorrer a lista de imagens e obter as datas e valores de precipitacao
    for i in range(precipitation.size().getInfo()):
        image = ee.Image(precipitation.toList(precipitation.size()).get(i))
        data = ee.Date(image.get('system:time_start')).format('yyyy-MM-dd').getInfo()
        ano = data.split('-')[0]

        # Verificar se o ano mudou
        if ano != ano_atual:
            ano_atual = ano
            num_pentada = 1
            valores_por_ano[ano] = []
        else:
            num_pentada += 1

        valor = image.reduceRegion(ee.Reducer.sum(), geometry=ee.Geometry.Point([-64.02760881257484, -4.436083218695817])).get('precipitation').getInfo()
        valores_por_ano[ano].append(valor)

    # Criar um DataFrame a partir do dicionario de valores por ano
    df_pentada = pd.DataFrame(valores_por_ano)

    # Adicionar uma coluna de Pentada
    df_pentada["Pentada"] = [f"{i}º" for i in range(1, len(df_pentada) + 1)]

    return df_pentada

# Definir datas de inicio e fim 
dataInicio = datetime.strptime("01-01-2000", "%d-%m-%Y")
dataFim = datetime.strptime("01-02-2010", "%d-%m-%Y")


# Chamar a função para calcular a pentada
df_pentada = calcula_pentada(dataInicio, dataFim)

# Salvar o DataFrame no arquivo Excel
df_pentada.to_excel('pentada_amazonia_atualizada_2024.xlsx', index=False)
