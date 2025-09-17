def estatisticas_basicas(df):
    print("\n=== Estatísticas básicas do clima ===")

    print("\nTemperatura (°C):")
    print(df["temperature"].describe())

    print("\nUmidade Relativa (%):")
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

    print(f"Temperatura média: {media_temp:.2f} °C")
    print(f"   Máxima: {max_temp:.2f} °C")
    print(f"   Mínima: {min_temp:.2f} °C")

    print(f"\nUmidade média: {media_hum:.2f}%")
    print(f"   Máxima: {max_hum:.2f}%")
    print(f"   Mínima: {min_hum:.2f}%")