"""
Created on Tues Mar  13 01:00:00 2018

@author: shreyak

app to receive POST request from data center to centeralized server
"""

import json
import config
import os
import DumpData

from flask import Flask, request, abort, Response
from flask_cors import CORS
from flask import send_from_directory

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def test():
    return "Server is running"


@app.route("/registerResource", methods=['POST'])
def register_resource():
    try:
        body = request.get_json()
        hostname = body['hostname']
        interfaces = body['interfaces']
        os_info = body['osinfo']
        open_ports = body['openports']
        cpu_info = body['cpuinfo']
        print('Details of the data center')
        print(' ')
        print('Hostname:', hostname)
        print(' ')
        print('Interfaces:import json', interfaces)
        print(' ')
        print('os info: ', os_info)
        print(' ')
        print('ports which are opened: ', open_ports)
        print(' ')
        print('cpu info:', cpu_info)
    except Exception as e:
        msg = 'Bad json format ' + str(e)
        error_msg = {'message': msg}
        abort(400, error_msg)

    json_obj = json.dumps(body)
    obj = DumpData.DumpData()
    obj.save_json(json_obj)

    json_body = {'message': 'Success'}
    return Response(json_body, mimetype='application/json')

@app.route('/agent/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, config.env['AGENT'])
    return send_from_directory(directory=uploads, filename=filename)

if __name__ == '__main__':
    print("App is running in %s on port %s" % (config.env['ENVIRONMENT'], config.env['PORT']))
    # app.run(host=config.env['HOSTNAME'], port=config.env['PORT'])
    app.run()

app.config['DEBUG'] = True
