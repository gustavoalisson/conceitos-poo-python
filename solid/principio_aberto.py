# Exemplo de princípio aberto            
class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

class Malabarista:
    def apresentar_show(self):
        print('Malabarista apresentando o seu show!')


class Palhaco:
    def apresentar_palhaco(self):
        print('Palhaço apresentando o seu show!') 
        

circo = Circo()        
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)

