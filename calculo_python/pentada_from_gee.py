# O objetivo deste programa eh coletar dados de precipitacao em uma regiao definida, 
# a fim de se construir uma base de dados que registre a acumulacao de chuva em intervalos
# de 5 dias, durante um período continuo de 305 dias. Na terminologia climatologica, esses 
# intervalos sao referidos como "pentadas".

# importacao do google earth engine
import ee
import pandas as pd
from datetime import datetime, timedelta

def calcula_pentada(dataInicio, dataFim, coordenadas):
    # Autenticação e inicialização da API
    ee.Authenticate()
    ee.Initialize()
    
    # Definir intervalo de tempo
    intervalo = 5

    # Base utlizada para a coleta de dados
    # Grupo de Riscos Climaticos Precipitacao por infravermelho com dados da estacao (CHIRPS).
    satelite = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY")

    # Base de extracao
    regiao = ee.Geometry.Rectangle(coordenadas)
    dadosFiltrados = satelite.filterBounds(regiao).filterDate(dataInicio, dataFim)
    bandasSelecionadas = dadosFiltrados.select(["precipitation"])
    
    # Definir listas para armazenar datas e acumulações
    datas = []
    acumulados = []
    
    # Iterar sobre as datas para calcular o acumulado
    data_corrente = dataInicio
    while data_corrente <= dataFim:
        data_final_intervalo = data_corrente + timedelta(days=intervalo)
        
        # Filtrar as imagens dentro do intervalo
        imagens_intervalo = bandasSelecionadas.filterDate(data_corrente, data_final_intervalo)
        
        # Calcular a soma das imagens do intervalo
        acumulado = imagens_intervalo.sum().reduceRegion(
            reducer=ee.Reducer.sum(),
            geometry=regiao,
            scale=5000
        ).get("precipitation")
        
        # Adicionar a data e o acumulado às listas
        datas.append(data_corrente.strftime("%d-%m-%Y"))
        acumulados.append(acumulado.getInfo())
        
        data_corrente = data_final_intervalo + timedelta(days=1)
    
    # Criar um DataFrame com as datas e acumulados
    df = pd.DataFrame({"Data": datas, "Acumulado de Precipitação (mm)": acumulados})
    
    return df

# Local de estudo, as coordenadas devem estar em WGS 84 (latitude e longitude em graus decimais)
coordenadasAmazonia = [-70.1383, -9.7615, -55.9734, -3.4653] 

# Definir datas de inicio e fim 
dataInicio = datetime.strptime("01-01-2014", "%d-%m-%Y")
dataFim = dataInicio + timedelta(days=306)

# Chamar a função para calcular a pentada
df_pentada = calcula_pentada(dataInicio, dataFim, coordenadasAmazonia)
print(df_pentada)
