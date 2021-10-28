from modulos import Casa, Pessoa

casa = Casa()
pessoa_1 = Pessoa('Alisson')

pessoa_1.set_local(casa)
casa.set_propietario(pessoa_1)

proprietario = casa.get_proprietario()
proprietario.se_apresentar()

pessoa_1.apresentar_local()