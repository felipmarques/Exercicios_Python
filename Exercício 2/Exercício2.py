from classes import Carro

"""Crie uma classe que modele um carro 
(a) Atributos: marca, ano e preço 
(b) Métodos: mostrar preço e de exibição dos dados"""

carro1 = Carro('monza', 'chevrolet', 1996, 5000)
carro2 = Carro('fusca','volswagen', 1970, 3000)
carro1.registra_carro()
carro2.registra_carro()

print(Carro.mostra_preco('monza'))
print(Carro.mostra_preco('fusca'))


