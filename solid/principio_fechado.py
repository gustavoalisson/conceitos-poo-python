# Principio aberto e fechado 

# Exemplo de princípio fechado
class Circo:
    
    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()
    
    def apresentar_malabarista(self):
        print('Malabarista apresentando o seu show!')
    
    def apresentar_palhaco(self):
        print('Palhaço apresentando o seu show!')

circo = Circo()
        
        
# Exemplo de princípio aberto            
class Circo2:
    
    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()
    
    def apresentar_malabarista(self):
        print('Malabarista apresentando o seu show!')
    
    def apresentar_palhaco(self):
        print('Palhaço apresentando o seu show!')

circo = Circo2()