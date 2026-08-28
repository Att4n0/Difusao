import pandas as pd

dados = pd.read_csv(
    "dados/substancias.csv",
    sep=";",
    decimal="."
)

nome = input("Digite o nome da substância: ").strip().lower()

substancia = dados[dados["nome"].str.strip().str.lower() == nome]

if substancia.empty:
    print("Substância não encontrada.")
else:
    print(substancia)