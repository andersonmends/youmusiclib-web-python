__author__ = 'Anderson'
from dao.ConnectionFactory import ConnectionFactory
from modelo.Usuario import Usuario

class UsuarioDAO():
    def __init__(self):
        factory = ConnectionFactory()
        self.conn = factory.get_connection()

    def buscar_por_email(self, email):

        usuario = Usuario()

        try:

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM USUARIO WHERE EMAIL ='%s'" % email)
            dados = cursor.fetchone()

            usuario.nome = dados[0]
            usuario.email = dados[1]
            usuario.senha = dados[2]

        except Exception as e:
            self.__erro = str(e)

        self.conn.close()

        return usuario

    def adicionar(self, usuario):

        try:

            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO USUARIO VALUES('%s','%s','%s')" % (usuario.nome, usuario.senha, usuario.email))
            self.conn.commit()
            print ("adicionado")

        except Exception as e:
            self.__erro = str(e)
            print ("nao adicionado")

        self.conn.close()

    def listar_usuarios(self):
        metodo = None

    def remover(self, usuario):

        metodo = None

    def atualizar(self, usuario):

        metodo = None
