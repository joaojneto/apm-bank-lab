from flask import Flask, render_template, request
from datetime import datetime, timedelta
from elasticapm.contrib.flask import ElasticAPM
import os

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': os.environ.get('SERVICE_NAME', 'unknow'),
  'SECRET_TOKEN': 'YOUR_SECRET_TOKEN_HERE',
  'SERVER_URL': 'https://endpoint_apm.apm.us-central1.gcp.cloud.es.io:443',
  'ENVIRONMENT': os.environ.get('ENV', 'unknow'),
}
apm = ElasticAPM(app)

def spendingTime(tempoAtual):
    segundos = 0
    while segundos < 10:
        1 + 1
        tempSec = datetime.now()
        diferenca = tempSec - tempoAtual
        diferenca_timedelta = timedelta(days=diferenca.days, seconds=diferenca.seconds)
        
        segundos = diferenca_timedelta.seconds % 60
        print(segundos)
    
def calcEx(num1,num2):
    tempoAtual = datetime.now()
    spendingTime(tempoAtual)
    return num1 + num2

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtem os numeros digitados pelo usuario
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        
        # Calcula a soma dos numeros
        resultado = calcEx(num1,num2)
        
        # Retorna a pagina de resultado com o valor calculado
        return render_template('resultado.html', resultado=resultado)
    
    # Se o metodo for GET, exibe o formulario para inserir os numeros
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
