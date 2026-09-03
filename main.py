import os
import subprocess
import pandas as pd

dados = pd.read_csv(
    "dados/tabelak2.csv",
    sep=";",
    decimal="."
)

def limpa_tela():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])

def encontrar_substancia():
    nome = input("Digite o nome da substância: ").strip().lower()

    substancia = dados[dados["nome"].str.strip().str.lower() == nome]

    if substancia.empty:
        print("Substância não encontrada.")
    else:
        print(substancia)

if __name__ == '__main__':
    limpa_tela()
    encontrar_substancia()