class Produto:
  def __init__(self, nome, preco):
      self.nome = nome
      self.preco = preco
  
  def desconto(self, percentual):
      self.preco = self.preco - (self.preco * (percentual / 100))
  
  @property
  def nome(self):
      return self._nome
  
  @nome.setter
  def nome(self, valor):
      texto = valor.capitalize()
      self._nome = texto
       
  #Getter
  @property
  def preco(self):
      return self._preco
  
  # Setter
  @preco.setter
  def preco(self, valor):
      if isinstance(valor, str):
          valor = float(valor.replace('R$', ''))
      self._preco = valor
           

p1 = Produto('CANECA', 50)
p1.desconto(10)
print(p1.nome,p1.preco)      

p2 = Produto('CAMISA', 'R$10')
p2.desconto(6)
print(p1.nome,p2.preco)           