# Importações
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    """Calcula o consumo estimado com base na área, alterando comentário de exemplo.

    Args:
        size (int): Tamanho (área) da residência
        lights (int): Quantidade de luminárias
        device (int): Quantidade de aparelhos

    Returns:
        float: Consumo estimado
    """
    # Coeficientes usados no cálculo do consumo de energia
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + device * devices_coef

# A primeira página
@app.route('/')
def index():
    return render_template('index.html')

# A segunda página
@app.route('/<int:size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# A terceira página
@app.route('/<int:size>/<int:lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )

# Cálculo
@app.route('/<int:size>/<int:lights>/<int:device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(size,
                                                    lights,
                                                    device
                                                    )
                        )

# O formulário
@app.route('/form')
def form():
    return render_template('form.html')

# Resultados do formulário
@app.route('/submit', methods=['POST'])
def submit_form():
    return render_template('form_result.html',
                           name=request.form['name'],
                           email=request.form['email'],
                           address=request.form['address'],
                           date=request.form['date'],
                           )

if __name__ == '__main__':
    app.run(debug=True)
