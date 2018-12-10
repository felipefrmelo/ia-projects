from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from json import dumps

# Ler modulo proprio
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/src')
# import textmining_code

# Lidar com Chamada Assincrona
app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin
def hello():
    return 'Hello, World!'

@app.route('/test2', methods = ['POST'])
@cross_origin()
def call_test():
	# agent = {'position': request.json['startState'],
	# 		'dirty' : {'A': request.json['dirtyA'], 'B': request.json['dirtyB'] }}
	# return jsonify(request.json)

	return jsonify({'x': request.json})
	# return jsonify(textmining_code.test_string(agent)) # retorna como JSON

@app.route('/test2', methods = ['GET'])
@cross_origin()
def my_test():
	return jsonify({'x': 'x', 'y': 'y'})

	
if __name__ == '__main__':
	app.run(debug=True)