from Exercício2 import Carro

carro1 = Carro('monza', 'chevrolet', 1996, 5000)
carro2 = Carro('fusca','volswagen', 1970, 3000)
carro1.registra_carro()
carro2.registra_carro()

print(Carro.mostra_preco('monza'))
print(Carro.mostra_preco('fusca'))


