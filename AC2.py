from flask import Flask, jsonify,request

app = Flask(__name__)

carros = [
    {
        'id': 1,
        'marca': 'BMw',
        'modelo': 'X5'
    },
    {
        'id': 2,
        'marca': 'Hyanduai',
        'modelo': 'Azera '
    },
    {
        'id': 3,
        'marca': 'Ford',
        'modelo': 'Escort-SR'
    },
    {
        'id': 4,
        'marca': 'Tesla',
        'modelo': 'Model-3'
    },
]

@app.route('/carros',methods=['GET'])
def obter_carros():
    return jsonify(carros)


@app.route('/carros/<int:id>',methods =['GET'])
def obter_carros_por_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)

            
               
app.run(port=5000,host='localhost',debug=True)

