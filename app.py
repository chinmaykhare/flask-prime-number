from flask import Flask, request, jsonify
import helper_methods
import os

dbHostname = os.environ['MYSQL_HOSTNAME']

app = Flask(__name__)

@app.route('/home')
def home():
    return jsonify({'result': 'It works'})

@app.route('/checkPrime', methods=['GET'])
def checkPrime():
    args = request.args
    num1 = args['num1']
    result = helper_methods.checkPrimeNumber(int(num1))
    helper_methods.insertResult(dbHostname,str(num1),str(result))
    return jsonify({'The entered number is': str(result)})


@app.route('/initializeDb')
def intializeDb():
    helper_methods.initializeDb(dbHostname)
    return jsonify('DB Initialized')

if __name__ == "__main__":
    app.run(debug=True, port=9000, host='0.0.0.0')
