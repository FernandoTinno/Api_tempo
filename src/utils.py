from api import DATA_DIR

def salvar_csv(df):
    output_file = DATA_DIR / "clima.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Arquivo CSV salvo em: {output_file}")