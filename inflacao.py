import pandas as pd
import matplotlib.pyplot as plt

# 1. Cesta básica (preço nominal)
cesta = pd.read_csv("cesta_basica_bh.csv")
cesta["data"] = pd.to_datetime(cesta["data"]).dt.to_period("M")

# 2. IPCA mensal (%), direto do Banco Central
url = ("https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados"
       "?formato=json&dataInicial=01/01/1998&dataFinal=30/06/2025")
ipca = pd.read_json(url)
ipca["data"] = pd.to_datetime(ipca["data"], format="%d/%m/%Y").dt.to_period("M")
ipca["valor"] = ipca["valor"].astype(float)

# 3. Índice acumulado (calculado ANTES do merge, com todos os meses)
ipca["indice"] = (1 + ipca["valor"] / 100).cumprod()

# 4. Juntar e converter pra reais de jun/2025
df = cesta.merge(ipca, on="data")
indice_final = df["indice"].iloc[-1]
df["cesta_real"] = df["valor_cesta_bh"] * indice_final / df["indice"]

print(len(df))
print(df[["data", "valor_cesta_bh", "cesta_real"]].iloc[[0, -1]])

# 5. Gráfico: nominal vs real
x = df["data"].dt.to_timestamp()
plt.plot(x, df["valor_cesta_bh"], label="Nominal")
plt.plot(x, df["cesta_real"], label="Real (R$ de jun/2025)")
plt.title("Cesta básica em Belo Horizonte: nominal vs. real")
plt.ylabel("R$")
plt.legend()
plt.savefig("grafico_real.png")