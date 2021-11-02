__author__ = 'Anderson'

from modelo.Usuario import Usuario
from dao.UsuarioDAO import UsuarioDAO
from modelo.Musica import Musica
from dao.MusicaDAO import MusicaDAO

usuario = Usuario()
usuario.email = "anderson.mends@gmail.com"
usuario.nome = "teste"
usuario.senha = ""

# dao = UsuarioDAO()
# usuario = dao.buscar_por_email(usuario)

# dao.adicionar(usuario)
# print usuario.nome

# musica = Musica()
# musica.nome = "sou foda"
# musica.duracao = 100
# musica.caminho = "sou foda 2"
# musica.tamanho = 100
#
dao = MusicaDAO()
# # dao.adicionar(musica, usuario)
musicas = []
#

musicas = dao.listar_musicas(usuario)
for mus in musicas:

    print (mus.nome)
