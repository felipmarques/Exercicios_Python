"""Escreva um programa que simule o carrinho de compras de um site:

1.Tenha alguns produtos disponíveis.
2.Adicione produtos no carrinho.
3.Liste os produtos que estão no carrinho.
4.Mostre o total a ser pago."""

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = float(valor)

class CarrinhoDeCompras:
    def __init__(self,):
        self._produtos = []

    def compra_produto(self, produto):
        self._produtos.append(produto)

    def mostra_produtos(self):
        for produto in self._produtos:
            print(f'{produto.nome}, R${produto.valor: 0.2f}')

    def total(self):
        total = 0
        for produto in self._produtos:
            total += produto.valor
        print(f'O total é R${total: 0.2f}')


