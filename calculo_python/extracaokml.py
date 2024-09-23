import geopandas as gpd
import ee
import pandas as pd
from datetime import datetime

# Carregar o arquivo KML usando GeoPandas
kml_file = "/home/talita/Documentos/tgi/areasDesmatadas/kml/areaDesmat_Area1.kml"
gdf = gpd.read_file(kml_file, driver='KML')

# Extraindo a geometria da área de interesse (supondo que há uma única geometria no KML)
area_de_interesse = gdf.geometry[0]

# Converter a geometria para o formato GeoJSON que o GEE pode entender
geojson_geometry = ee.Geometry.Polygon(list(area_de_interesse.exterior.coords))

def calcula_pentada(dataInicio, dataFim, geometry):
    # Autenticação e inicialização da API
    ee.Authenticate()
    ee.Initialize()

    # Base utilizada para a coleta de dados
    dataset = ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD').filterDate(dataInicio, dataFim)

    # Selecionar a banda de precipitação
    precipitation = dataset.select('precipitation')

    # Inicializar variáveis para rastrear o ano e a numeração da pentada
    ano_atual = None
    num_pentada = 0

    # Criar um dicionário para armazenar os valores de precipitação por ano
    valores_por_ano = {}

    # Percorrer a lista de imagens e obter as datas e valores de precipitação
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

        # Calcular o valor de precipitação na área de interesse (definida pelo KML)
        valor = image.reduceRegion(ee.Reducer.sum(), geometry).get('precipitation').getInfo()
        valores_por_ano[ano].append(valor)

    # Criar um DataFrame a partir do dicionário de valores por ano
    df_pentada = pd.DataFrame(valores_por_ano)

    # Adicionar uma coluna de Pentada
    df_pentada["Pentada"] = [f"{i}º" for i in range(1, len(df_pentada) + 1)]

    return df_pentada

# Definir datas de início e fim 
dataInicio = datetime.strptime("01-01-2010", "%d-%m-%Y")
dataFim = datetime.strptime("01-01-2020", "%d-%m-%Y")

# Chamar a função para calcular a pentada usando a geometria do KML
df_pentada = calcula_pentada(dataInicio, dataFim, geojson_geometry)

# Salvar o DataFrame no arquivo Excel
df_pentada.to_excel('pentada_amazonia_atualizada_2024.xlsx', index=False)
