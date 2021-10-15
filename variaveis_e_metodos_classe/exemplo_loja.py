class Loja:
    
    tarifa = 1.03
    
    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco 
    
    def apresentar_endereco(self) -> None:
        print(f' Endereço: {self.__endereco}')
    
    @classmethod
    def vender(cls) -> int:
        return 60 * cls.tarifa
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa

loja_praia = Loja('Praia')   
loja_centro = Loja('Centro')                 

loja_praia.apresentar_endereco()

print(loja_praia.vender())
print(loja_centro.vender())

loja_centro.alterar_tarifa(1.50)

print(loja_praia.vender())
print(loja_centro.vender())


print('__________________________________________________')

# ! EXEMPLO SEM USAR O CONTEXTO DE CLASSE

class Loja2:
    
    tarifa = 1.03
    
    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco 
    
    def apresentar_endereco(self) -> None:
        print(f' Endereço: {self.__endereco}')
    
    def vender(self) -> int:
        return 60 * self.tarifa
    
    def alterar_tarifa(self, nova_tarifa: int) -> None:
        self.tarifa = nova_tarifa

loja_praia = Loja2('Praia')   
loja_centro = Loja2('Centro')                 

loja_praia.apresentar_endereco()

print(loja_praia.vender())
print(loja_centro.vender())

loja_centro.alterar_tarifa(1.50)

print(loja_praia.vender())
print(loja_centro.vender())