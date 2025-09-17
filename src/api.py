import requests
import json
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)

def baixar_clima():
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -23.55,
        "longitude": -46.63,
        "hourly": "temperature_2m,relative_humidity_2m"
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status() 
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