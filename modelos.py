import pandas as pd
import numpy as np

class Substancia:
    def __init__(self, nome, formula, massa_molar, ea_k, diametro_colisao, polar):
        self.nome = nome
        self.formula = formula
        self.massa_molar = massa_molar
        self.ea_k = ea_k
        self.diametro_colisao = diametro_colisao
        self.polar = polar

class DataBase:
    '''Importa os arquivos que compõe a base de dados do programa.'''

    def __init__(self, nome, caminho, sep=";", decimal="."):
        self._nome = nome
        self._caminho = caminho
        self._dados = pd.read_csv(caminho, sep=sep, decimal=decimal)

    def buscar_substancia(self, nome_substancia):
        termo = nome_substancia.strip().lower()
        resultado = self._dados[self._dados["nome"].str.strip().str.lower() == termo]

        if resultado.empty:
            return None

        linha = resultado.iloc[0]
        
        # Converte a linha encontrada direto num objeto Substancia!
        return Substancia(
            nome=linha["nome"],
            formula=linha["formula"],
            massa_molar=linha["massa_molar"],
            ea_k=linha["ea_k"],
            diametro_colisao=linha["diametro_colisao"],
            polar=linha["polar"]
        )