# O objetivo deste programa eh coletar dados de precipitacao em uma regiao definida, 
# a fim de se construir uma base de dados que registre a acumulacao de chuva em intervalos
# de 5 dias, durante um periodo continuo de 305 dias. Na terminologia climatologica, esses 
# intervalos sao referidos como "pentadas".

# importacao do google earth engine
import ee
ee.Authenticate()   
ee.Initialize()