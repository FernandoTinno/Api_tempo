import json
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def test_json_tem_dados():
    """Verifica se o JSON foi criado e contém dados"""
    with open(DATA_DIR / "clima.json", encoding="utf-8") as f:
        dados = json.load(f)
    assert "hourly" in dados
    assert "temperature_2m" in dados["hourly"]
    assert "relative_humidity_2m" in dados["hourly"]

def test_csv_tem_dados():
    """Verifica se o CSV foi criado e contém linhas"""
    df = pd.read_csv(DATA_DIR / "clima.csv")
    assert not df.empty
    assert "temperature" in df.columns
    assert "humidity" in df.columns

def test_graficos_existem():
    """Verifica se os gráficos foram criados"""
    assert (DATA_DIR / "grafico_temperatura.png").exists()
    assert (DATA_DIR / "grafico_umidade.png").exists()
    assert (DATA_DIR / "grafico_temp_umidade.png").exists()
