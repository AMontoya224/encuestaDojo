from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "estoessecreto"

listaFormulario = []

@app.route( '/', methods=['GET'] )
def paginaInicio():
    return render_template( "index.html")

@app.route( '/result', methods=["GET"] )
def despliegaDashboard():
    if 'nombre' in session:
        return render_template( "result.html", formulario=listaFormulario )
    else:
        return redirect( '/' )

@app.route( '/process', methods=["POST"] )
def registrarFormulario():
    nuevoFormulario = {
        "nombre" : request.form["nombre"],
        "locacion" : request.form["locacion"],
        "lenguaje" : request.form["lenguaje"],
        "comentario" : request.form["comentario"]
    }
    session["nombre"] = request.form["nombre"]
    session["locacion"] = request.form["locacion"]
    session["lenguaje"] = request.form["lenguaje"]
    session["comentario"] = request.form["comentario"]
    listaFormulario.append( nuevoFormulario )
    return redirect( '/result' )

@app.route( '/destroy_session', methods=["POST"] )
def borrarSession():
    session.clear()
    return redirect( '/' )

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo mas tarde"

if __name__ == "__main__":
    app.run(debug=True)