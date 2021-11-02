from flask import Flask, render_template, request, redirect, url_for
from dao.UsuarioDAO import UsuarioDAO
from modelo.Usuario import Usuario
from dao.MusicaDAO import MusicaDAO
from modelo.Musica import Musica

app = Flask(__name__)


@app.route("/index")
def index():

    dao = UsuarioDAO()
    usuario = dao.buscar_por_email("anderson.mends@gmail.com")
    musicas = []
    dao = MusicaDAO()
    musicas = dao.listar_musicas(usuario)
    return render_template("index.html", musicas=musicas)

    # return render_template("index.html")


@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")


@app.route('/main')
def main():
    try:
        return render_template("main.html")
    except Exception as e:
        return str(e)


@app.route("/connect")
def test_connect():
    try:
        usuario = Usuario()
        dao = UsuarioDAO()
        usuario = dao.buscar_por_email("anderson.mends@gmail.com")
        return render_template("index.html")

    except Exception as e:
        return str(e)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":

        # return request.form["cadastrar"]
        # return request.form["email"]

        try:
            if request.form["cadastrar"] is not None:
                return redirect(url_for('cadastrar'))
            else:
                return redirect(url_for("index"))

        except Exception as e:

            dao = UsuarioDAO()
            usuario = dao.buscar_por_email(request.form["email"])

            if usuario.email == request.form["email"] and usuario.senha == request.form["senha"]:
                musicas = []
                dao = MusicaDAO()
                musicas = dao.listar_musicas(usuario)
                return render_template("index.html", musicas=musicas)
                # return redirect(url_for("index", musicas = "teste"))
            else:
                return "Usuario nao cadastrado"


if __name__ == "__main__":
    app.run()
