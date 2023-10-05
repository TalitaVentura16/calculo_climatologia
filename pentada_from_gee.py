# O objetivo deste programa eh coletar dados de precipitacao em uma regiao definida, 
# a fim de se construir uma base de dados que registre a acumulacao de chuva em intervalos
# de 5 dias, durante um período continuo de 305 dias. Na terminologia climatologica, esses 
# intervalos sao referidos como "pentadas".

# importacao do google earth engine
import ee
import pandas as pd
from datetime import datetime, timedelta

def calcula_pentada(dataInicio, dataFim):
    import ee

    # Autenticação e inicialização da API
    ee.Authenticate()
    ee.Initialize()


    # Base utilizada para a coleta de dados
    # A base escolhida  é a CHIRPS - Grupo de Riscos Climaticos Precipitacao, os dados ja sao gerados com o intervado da
    # pentada.
    dataset = ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD') \
        .filterDate(dataInicio, dataFim)

    # Selecionar a banda de precipitacao
    precipitation = dataset.select('precipitation')

    # Obter informacoes das imagens e armazena em uma lista
    image_list = precipitation.toList(precipitation.size())

    # Inicializar variaveis para rastrear o ano e a numeracao da pentada
    ano_atual = None
    num_pentada = 0

    # Percorrer a lista de imagens e obter as datas e valores de precipitação
    datasValores = []
    for i in range(image_list.size().getInfo()):
        image = ee.Image(image_list.get(i))
        data = ee.Date(image.get('system:time_start')).format('yyyy-MM-dd').getInfo()
        ano = data.split('-')[0]

        # Verificar se o ano mudou
        if ano != ano_atual:
            ano_atual = ano
            num_pentada = 1
        else:
            num_pentada += 1

        valor = image.reduceRegion(ee.Reducer.sum(), geometry=ee.Geometry.Point([-64.02760881257484, -4.436083218695817])).get('precipitation').getInfo()
        datasValores.append((data, valor, f"{num_pentada}º"))

    # Imprimir as datas e valores
    for data, valor, num in datasValores:
        print(f"{data}, {valor}, {num}")

    return datasValores


# Definir datas de inicio e fim 
dataInicio = datetime.strptime("01-01-2014", "%d-%m-%Y")
dataFim = datetime.strptime("01-01-2016", "%d-%m-%Y")
##dataFim = dataInicio + timedelta(days=306)


# Chamar a funcao para calcular a pentada
df_pentada = calcula_pentada(dataInicio, dataFim)
valoresPentada = pd.DataFrame(df_pentada, columns=["Data", "Valor de Precipitação", "Pentada"])
print(valoresPentada)

# Salvar o DataFrame no arquivo Excel
valoresPentada.to_excel('pentada_amazonia.xlsx', index=False)
