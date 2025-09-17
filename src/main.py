from api import baixar_clima, carregar_dados
from process import estatisticas_basicas, calculos_aritmeticos
from plot import gerar_graficos
from utils import salvar_csv

if __name__ == "__main__":
    baixar_clima()
    df = carregar_dados()
    estatisticas_basicas(df)
    calculos_aritmeticos(df)
    gerar_graficos(df)
    salvar_csv(df)
