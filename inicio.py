from flask import Flask,render_template

app = Flask(__name__)

@app.route('/grafico')
def mostrar_grafico():
    return render_template('imigrante_brasil.html')

app.run(debug=True)
