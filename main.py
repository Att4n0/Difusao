import os
import subprocess
import pandas as pd

def limpa_tela():
    '''Limpa a tela, escolhendo o método pelo OS do usuário.'''
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])

def encontrar_substancia(df,nome):
    '''Retorna os dados de uma substância
    
    Inputs
    - Nome da substância
    - Nome do arquivo da busca

    Outputs
    -None, caso não o nome passado não seja encontrado no arquivo
    -Retorno das informações da substância no formato pandas.Series
    '''
    
    termo = nome.strip().lower()
    substancia = df[df["nome"].str.strip().str.lower() == termo]

    if substancia.empty:
        return None
    else:
        return(substancia)

if __name__ == '__main__':
    limpa_tela()

    dadosk2 = pd.read_csv("dados/tabelak2.csv", sep=";", decimal=".")

    nome_soluto = input('Digite o nome do soluto: ')
    soluto = encontrar_substancia(dadosk2, nome_soluto)

    nome_solvente = input('\nAgora, digite o nome do solvente: ')
    solvente = encontrar_substancia(dadosk2, nome_solvente)

    print('--- BUSCA DE COMPONENTES ---')

    if soluto is None:
        print(f"Erro: Soluto '{nome_soluto}' não foi encontrado no banco de dados.")

    if solvente is None:
        print(f"Erro: Solvente '{nome_solvente}' não foi encontrado no banco de dados.")
        
    if soluto is not None and solvente is not None:
        print(f'\nDados do soluto:\n{soluto}')
        print(f'\nDados od solvente:\n{solvente}')