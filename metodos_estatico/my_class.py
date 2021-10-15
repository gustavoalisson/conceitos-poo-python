# Um método estático não recebe um primeiro argumento implícito. 
#Um método estático também é um método vinculado à classe e não ao objeto da classe.
#Um método estático não pode acessar ou modificar o estado da classe.

class Error:

    @staticmethod
    def protocolo():
        print('Protocolo apresenta erro!') 
    
    @staticmethod
    def entrada():
        print('Parâmetros incorretos')       

Error.protocolo()