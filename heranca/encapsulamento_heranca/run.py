
# ? O que é uma variável protected ? 

# * protected = Acessível pela própria classe e pela sua herença, ou seja o filho herda os encapsulamentos protect da classe Pai
# * Os objetos protected não deveria ser visto pelos objetos instanciados dessas classes

# ! Explicação técnica
# * Variáveis ​​protegidas são os membros de dados de uma classe que podem
# * ser acessados ​​dentro da classe e as classes derivadas dessa classe.

# * Qualquer membro prefixado com um sublinhado deve ser tratado como uma parte não 
# * pública da API ou de qualquer código Python, seja uma função, um método ou um 
# * membro de dado.

class DatabaseConn:
    
    def __init__(self) -> None:
        self.__database = 'SQL Server'
        self._conn = '//connection_string'
        self.user = 'alisson'
    
    def get_database(self) -> None:
        print(self.get_database)
    
    def _testing_connection(self) -> None:
        print('Connection Ok!')

class Repository(DatabaseConn):
    
    def __init__(self) -> None:
        super().__init__()
        # print(self.user)
        # print(self.__database) # ! ERROR
        # print(self._conn)
    
    def select(self) -> None:
        self._testing_connection()
        print(f'connecting to {self._conn}')
        print(f'SELECT * FROM table')    

db = DatabaseConn()
# print(db.user)
# print(db.__database) # ! ERROR
# print(db._conn)

repo = Repository()
repo.select()

# ILUSTRAÇÃO DE ENCAPSULAMENTO

# *          PRIVATE     PROTECTED      PUBLIC
# * Classe      x            x             x
# * Herança                  x             x     
# * Objeto                                 x     

# ? OBSERVAÇÃO 

# * No Python é possível acessar um protected pelo objeto, mas o _ é usado como 
# * uma convenção entre Devs que não pode ser acessado em um objeto.