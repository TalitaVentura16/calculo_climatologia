import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import rcParams

# Configuração de fonte para o gráfico
rcParams['font.family'] = 'serif'

# Carregar os dados históricos
amazonia = '/home/talita/Documentos/calculo_climatologia/estudoEstacaoSeca/Dados/Amazonia_pentada_areaDematada3_precipitacao.xlsx'
df = pd.read_excel(amazonia)

# Dados sobre duração da estação seca já calculados previamente
# Assumindo que você já gerou o DataFrame `season_df` com as colunas ["Ano", "Duração_Seca"]

# Separar os dados de entrada (Ano) e saída (Duração_Seca)
X = season_df["Ano"].values.reshape(-1, 1)  # Transformar em matriz para o modelo
y = season_df["Duração_Seca"].values

# Criar e ajustar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Gerar projeções para os próximos 15 anos (2024 a 2038)
anos_futuros = np.arange(2024, 2039).reshape(-1, 1)  # Anos de 2024 a 2038
projecoes = modelo.predict(anos_futuros)

# Combinar anos futuros e projeções em um DataFrame
projecao_df = pd.DataFrame({
    "Ano": anos_futuros.flatten(),
    "Duração_Seca_Projetada": projecoes
})

# Plotar a duração da estação seca (histórico + projeções)
plt.figure(figsize=(12, 6))

# Dados históricos
plt.plot(season_df["Ano"], season_df["Duração_Seca"], marker="o", label="Duração Histórica", color="blue")

# Projeções
plt.plot(projecao_df["Ano"], projecao_df["Duração_Seca_Projetada"], marker="o", linestyle="--", label="Projeção", color="red")

# Configurações do gráfico
plt.title("Projeção da Duração da Estação Seca (Próximos 15 anos)", fontweight="bold", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Duração da Estação Seca (Pentadas)", fontsize=12)
plt.legend()
plt.grid(alpha=0.5)

# Salvar o gráfico
output_path_projection = "/home/talita/Documentos/calculo_climatologia/estudoEstacaoSeca/Resultados/Projecao_Duracao_Estacao_Seca.pdf"
plt.savefig(output_path_projection, format="pdf")

# Exibir o gráfico
plt.show()

# Exibir projeções
print(projecao_df)
