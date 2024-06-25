# Importa o framework Flask para criar a API
from flask import Flask, request, jsonify, render_template
# Importa o módulo json para trabalhar com dados JSON
import json

# Carrega os dados dos motociclistas do arquivo JSON
with open('riders.json', 'r') as f:
    riders = json.load(f)

# Cria um aplicativo Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('riders.html')

# Define o endpoint da API para obter os motociclistas
@app.route('/riders', methods=['GET'])
def get_riders():
    """
    Retorna uma lista de motociclistas filtrada pela cidade.

    Parâmetros:
        city: O nome da cidade para filtrar os motociclistas.

    Retorna:
        Uma lista de motociclistas no formato JSON.
    """

    # Obtém o parâmetro da cidade da consulta
    city = request.args.get('city')

    # Verifica se o parâmetro da cidade é "ALL"
    if city == "ALL":
        # Retorna todos os motociclistas
        return jsonify(riders)
    else:
        # Filtra os motociclistas pela cidade
        filtered_riders = [rider for rider in riders if rider['city'] == city]

        # Verifica se algum motociclista foi encontrado
        if not filtered_riders:
            return jsonify({'error': 'Nenhum motociclista encontrado na cidade fornecida.'}), 404

        # Retorna os motociclistas filtrados como JSON
        return jsonify(filtered_riders)

# Define an new endpoint to get riders from Belo Horionte /rider/bh 
@app.route('/riders/bh', methods=['GET'])
def get_riders_bh():
    """
    Retorna uma lista de motociclistas de Belo Horizonte.

    Retorna:
        Uma lista de motociclistas no formato JSON.
    """

    # Filtra os motociclistas de Belo Horizonte
    bh_riders = [rider for rider in riders if rider['city'] == 'Belo Horizonte']

    # Verifica se algum motociclista foi encontrado
    if not bh_riders:
        return jsonify({'error': 'Nenhum motociclista encontrado em Belo Horizonte.'}), 404

    # Retorna os motociclistas de Belo Horizonte como JSON
    return jsonify(bh_riders)


# Inicia o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
