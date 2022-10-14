arq = "Dados dos Carros"

"""Crie uma classe que modele um carro 
(a) Atributos: marca, ano e preço 
(b) Métodos: mostrar preço e de exibição dos dados"""

class Carro:
    def __init__(self, modelo, marca, ano, preco):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._preco = preco

    def registra_carro(self):
        """Optei por manipular os dados dos carros através de arquivos.txt"""
        try:
            a = open(arq, 'at')
        except FileNotFoundError:
            print("Erro ao ler arquivo")
        else:
            a.write(f'{self._marca} {self._modelo} {self._ano}, valor: R${self._preco}' + '\n')
            a.close()

    @staticmethod
    def mostra_preco(carro):
        carro = carro
        with open(arq) as a:
            datafile = a.readlines()
        for line in datafile:
            if carro in line:
                return f'o valor do {carro} é {line[-7:]}'
