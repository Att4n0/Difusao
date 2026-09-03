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

def solicitar_substancias(db_propriedades):
    """Função auxiliar para pedir e validar as substâncias."""
    nome_soluto = input("Digite o nome do soluto: ").strip()
    nome_solvente = input("Digite o nome do solvente: ").strip()

    soluto = db_propriedades.buscar_substancia(nome_soluto)
    solvente = db_propriedades.buscar_substancia(nome_solvente)

    if soluto is None:
        print(f"Erro: Soluto '{nome_soluto}' não encontrado.")
    if solvente is None:
        print(f"Erro: Solvente '{nome_solvente}' não encontrado.")

    return soluto, solvente

def exibir_dados_substancias(db_propriedades):
    """Opção 1 do Menu: Apenas exibe as propriedades no terminal."""
    soluto, solvente = solicitar_substancias(db_propriedades)
    
    if soluto and solvente:
        print(f"\n--- SOLUTO: {soluto.nome} ({soluto.formula}) ---")
        print(f"Massa Molar: {soluto.massa_molar} g/mol")
        print(f"Epsilon/k: {soluto.ea_k} K")
        print(f"Diâmetro (sigma): {soluto.diametro_colisao} Å")
        
        print(f"\n--- SOLVENTE: {solvente.nome} ({solvente.formula}) ---")
        print(f"Massa Molar: {solvente.massa_molar} g/mol")
        print(f"Epsilon/k: {solvente.ea_k} K")
        print(f"Diâmetro (sigma): {solvente.diametro_colisao} Å")

if __name__ == '__main__':
    limpa_tela()

    tabelak2 = DataBase("Propriedades", "dados/tabelak2.csv", sep=";", decimal=".")
    tabelak1 = DataBase("IntegralColisao", "dados/tabelak1.csv", sep=";", decimal=",")

    exibir_dados_substancias(tabelak2)
    