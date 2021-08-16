
# * Associação - Usa
# * Agregação - Tem
# * Composição - É dono
# * Herança - É
from classes import Produto, Carrinho_De_Compras

carrinho = Carrinho_De_Compras()
p1 = Produto('Camiseta Broomer', 200)
p2 = Produto('Iphone XS', 7200)
p3 = Produto('Calça Broomer', 280)


carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)


carrinho.listar_produtos()
print(carrinho.soma_total())

