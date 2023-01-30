import flask 
from flask import request, jsonify
from numToString import numToString

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/<num>', methods=['GET'])
def sample(num='1'):
    try:
        num = int(num)
        return jsonify({'value':numToString().int2str(num)})
    except:
        return jsonify({'error':f'invalid input: {str(num)}'})
    # return 'hwllow world'

app.run()