""" Utilizando o método de composição crie duas classes (Cliente e Endereço)
que simulem o cadastro do endereço de um cliente
"""

class Cliente:
    def __init__(self, nome):
        self._nome = nome
        self._enderecos = []

    def cad_endereco(self, cidade):
        self._enderecos.append(Endereco(cidade))

    def mostra_endereco(self):
        for endereco in self._enderecos:
            print(f'{self._nome} reside em {endereco.cidade}')

class Endereco:
    def __init__(self, cidade):
        self._cidade = cidade

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade
