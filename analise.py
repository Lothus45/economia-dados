import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cesta_basica_bh.csv")
df["data"] = pd.to_datetime(df["data"])

plt.plot(df["data"], df["valor_cesta_bh"])
plt.title("Custo da cesta básica em Belo Horizonte (1998-2025)")
plt.ylabel("R$")
plt.savefig("grafico.png")