import pandas as pd
import matplotlib.pyplot as plt
from api import DATA_DIR

def gerar_graficos(df):
    df["time"] = pd.to_datetime(df["time"])

    print("\n=== Gerando gráficos... ===")

    # 1. Temperatura ao longo do tempo
    plt.figure(figsize=(12, 6))
    plt.plot(df["time"], df["temperature"], label="Temperatura (°C)", color="red")
    plt.xlabel("Tempo")
    plt.ylabel("Temperatura (°C)")
    plt.title("Variação da Temperatura ao longo do tempo")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(DATA_DIR / "grafico_temperatura.png")
    plt.show()

    # 2. Umidade ao longo do tempo
    plt.figure(figsize=(12, 6))
    plt.plot(df["time"], df["humidity"], label="Umidade (%)", color="blue")
    plt.xlabel("Tempo")
    plt.ylabel("Umidade Relativa (%)")
    plt.title("Variação da Umidade ao longo do tempo")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(DATA_DIR / "grafico_umidade.png")
    plt.show()

    # 3. Temperatura x Umidade (dispersão)
    plt.figure(figsize=(8, 6))
    plt.scatter(df["temperature"], df["humidity"], alpha=0.6, color="green")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Umidade (%)")
    plt.title("Relação entre Temperatura e Umidade")
    plt.tight_layout()
    plt.savefig(DATA_DIR / "grafico_temp_umidade.png")
    plt.show()
    return df