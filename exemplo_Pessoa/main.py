from pessoa import Pessoa

# p1 = Pessoa('Alisson', 24)
p2 = Pessoa('Pedro', 21)

# p1.falar('Olá tudo bem ?')
# p2.falar('Tudo bem!!!')
# p1.falar('Como vai você ?')
# p2.falar('Muito bem!')
# p1.get_ano_nascimento()

# ! Testando método da classe

# pessoa = Pessoa.por_ano_nascimento('João', 1998)
# print(pessoa.nome, pessoa.idade)

# ! Testando método estático

gerador = Pessoa.gera_id_pessoa()

print(gerador)
