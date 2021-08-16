# 
# * Associação - Usa
# * Agregação - Tem
# * Composição - É dono
# * Herança - É

from classes import Cliente

cliente1 = Cliente('Luiz', 11231231, 23)
print(cliente1.nome)
cliente1.insere_endereco('Recife', 'PE')
cliente1.lista_enderecos()
del cliente1
print()
cliente2 = Cliente('Rafael', 23423444, 52)
print(cliente2.nome)
cliente2.insere_endereco('Guarulhos', 'SP')
cliente2.lista_enderecos()
print()
cliente3 = Cliente('Alisson', 234233334, 24)
print(cliente3.nome)
cliente3.insere_endereco('Jaboatão dos Guararapes', 'PE')
cliente3.lista_enderecos()


print()
print('#################################################')