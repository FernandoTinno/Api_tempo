import requests
import json
import time
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)

def baixar_clima():
    """Baixa dados do Open-Meteo e salva em JSON"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -23.55,
        "longitude": -46.63,
        "hourly": "temperature_2m,relative_humidity_2m"
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()  # gera erro se status != 200
        dados = resp.json()

        with open(DATA_DIR / "clima.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print(f"Arquivo salvo em {DATA_DIR / 'clima.json'}")

    except requests.exceptions.Timeout:
        print("Erro: A requisição demorou muito para responder (timeout).")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def carregar_dados():
    """Carrega JSON salvo e converte para DataFrame"""
    try:
        with open(DATA_DIR / "clima.json", encoding="utf-8") as f:
            dados = json.load(f)

        if "hourly" not in dados:
            raise ValueError("JSON não contém dados 'hourly'.")

        df = pd.DataFrame({
            "time": dados["hourly"]["time"],
            "temperature": dados["hourly"]["temperature_2m"],
            "humidity": dados["hourly"]["relative_humidity_2m"]
        })

        return df

    except FileNotFoundError:
        print("Erro: Arquivo clima.json não encontrado. Rode baixar_clima() antes.")
    except ValueError as e:
        print(f"Erro de conteúdo: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def estatisticas_basicas(df):
    print("\n=== Estatísticas básicas do clima ===")

    print("\n🌡️ Temperatura (°C):")
    print(df["temperature"].describe())

    print("\n💧 Umidade Relativa (%):")
    print(df["humidity"].describe())

    return df

def calculos_aritmeticos(df):
    print("\n=== Cálculos aritméticos ===")

    media_temp = df["temperature"].mean()
    max_temp = df["temperature"].max()
    min_temp = df["temperature"].min()

    media_hum = df["humidity"].mean()
    max_hum = df["humidity"].max()
    min_hum = df["humidity"].min()

    print(f"🌡️ Temperatura média: {media_temp:.2f} °C")
    print(f"   Máxima: {max_temp:.2f} °C")
    print(f"   Mínima: {min_temp:.2f} °C")

    print(f"\n💧 Umidade média: {media_hum:.2f}%")
    print(f"   Máxima: {max_hum:.2f}%")
    print(f"   Mínima: {min_hum:.2f}%")

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


def salvar_csv(df):
    output_file = DATA_DIR / "clima.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"📂 Arquivo CSV salvo em: {output_file}")


if __name__ == "__main__":
    inicio = time.time()
    baixar_clima()
    df = carregar_dados()
    df = estatisticas_basicas(df)
    calculos_aritmeticos(df)
    gerar_graficos(df)
    salvar_csv(df)
    fim = time.time()
    print(f"tempo total de execução: {fim- inicio:.2f} segundos")
