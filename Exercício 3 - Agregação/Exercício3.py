from classes import Produto, CarrinhoDeCompras

"""Escreva um programa que simule o carrinho de compras de um site:

1.Tenha alguns produtos disponíveis.
2.Adicione produtos no carrinho.
3.Liste os produtos que estão no carrinho.
4.Mostre o total a ser pago."""

p1 = Produto('Nescau', 5.00)
p2 = Produto('Margarina', 4.00)
p3 = Produto('Leite Condensado', 3.00)
p4 = Produto('Chocolate granulado', 4.00)

carrinho = CarrinhoDeCompras()
carrinho.compra_produto(p1)
carrinho.compra_produto(p2)
carrinho.compra_produto(p3)
carrinho.compra_produto(p4)

carrinho.total()
carrinho.mostra_produtos()


