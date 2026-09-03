import os
import subprocess
import pandas as pd
from modelos import DataBase, Substancia

def limpa_tela():
    '''Limpa a tela, escolhendo o método pelo OS do usuário.'''
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])

if __name__ == '__main__':
    limpa_tela()

    tabelak2 = DataBase("Propriedades", "dados/tabelak2.csv", sep=";", decimal=".")
    tabelak1 = DataBase("IntegralColisao", "dados/tabelak1.csv", sep=";", decimal=",")

    nome_soluto = input("Digite o nome do soluto: ")
    nome_solvente = input("Digite o nome do solvente: ")

    soluto = tabelak2.buscar_substancia(nome_soluto)
    solvente = tabelak2.buscar_substancia(nome_solvente)

    if soluto is not None and solvente is not None:
        print(f"\nSoluto encontrado: {soluto.nome} (Fórmula molecular = {soluto.formula}) (M = {soluto.massa_molar} g/mol)")
        print(f"Solvente encontrado: {solvente.nome} (Fórmula molecular = {solvente.formula}) (M = {solvente.massa_molar} g/mol)")

    if soluto is None:
       print(f"Erro: Soluto '{nome_soluto}' não foi encontrado no banco de dados.")
    if solvente is None:
       print(f"Erro: Solvente '{nome_solvente}' não foi encontrado no banco de dados.")