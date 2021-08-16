class Carrinho_De_Compras:
    def __init__(self):
        self.produtos = []
        
    def inserir_produto(self, produto):
        self.produtos.append(produto)
     
    def listar_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome} - R${produto.valor}')
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:        
            total += produto.valor
        return total    
                
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
        