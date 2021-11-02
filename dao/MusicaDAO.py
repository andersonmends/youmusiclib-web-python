__author__ = 'Anderson'
from dao.ConnectionFactory import ConnectionFactory
from modelo.Musica import Musica


class MusicaDAO():
    def __init__(self):
        factory = ConnectionFactory()
        self.conn = factory.get_connection()

    def buscar_por_id(self, id):
        metodo = None

    def adicionar(self, musica, usuario):

        try:

            cursor = self.conn.cursor()
            cursor.execute("insert into musica values (null,'%s','%s','%s','%s','%s')" % (
                musica.nome, musica.duracao, musica.tamanho, musica.caminho, usuario.email))
            self.conn.commit()
            print ("adicionado")

        except Exception as e:
            self.__erro = str(e)

        self.conn.close()

    def listar_musicas(self, usuario):

        musicas = []

        try:

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM musica WHERE email = '%s'" % usuario.email)
            dados = cursor.fetchall()
            # print dados

            for dado in dados:
                musica = Musica()
                musica.nome = dado[1]
                musica.duracao = dado[2]
                musica.tamanho = dado[3]
                musica.caminho = dado[4]

                musicas.append(musica)

        except Exception as e:
            self.__erro = str(e)

        self.conn.close()

        return musicas

    def remover(self, usuario):
        metodo = None

    def atualizar(self, usuario):
        metodo = None
