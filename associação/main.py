
# * Associação - Usa (Quando um objeto navega para a utilização de outro objeto)
# * Agregação - Tem
# * Composição - É dono
# * Herança - É

from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

# escritor.ferramenta = maquina
# escritor.ferramenta.escrever()