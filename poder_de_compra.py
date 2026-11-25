import pandas as pd
import matplotlib.pyplot as plt
cesta = pd.read_csv("cesta_basica_bh.csv")
cesta["data"] = pd.to_datetime(cesta["data"]).dt.to_period("M")
url = ("https://api.bcb.gov.br/dados/serie/bcdata.sgs.1619/dados"
       "?formato=json&dataInicial=01/01/1998&dataFinal=30/06/2025")
sm = pd.read_json(url)
sm["data"] = pd.to_datetime(sm["data"], format="%d/%m/%Y").dt.to_period("M")
sm["valor"] = sm["valor"].astype(float)
sm = sm.rename(columns={"valor": "salario_minimo"})
df = cesta.merge(sm, on="data")
df["cestas_por_salario"] = df["salario_minimo"] / df["valor_cesta_bh"]
print(len(df))
print(df[["data", "cestas_por_salario"]].iloc[[0, -1]])
x = df["data"].dt.to_timestamp()
plt.plot(x, df["cestas_por_salario"])
plt.ylim(bottom=0)
plt.title("Quantas cestas básicas um salário mínimo compra (BH)")
plt.ylabel("Cestas por salário mínimo")
plt.savefig("grafico_poder_compra.png")