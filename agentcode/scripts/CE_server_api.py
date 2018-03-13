"""
Created on Tues Mar  13 01:00:00 2018

@author: shreyak

app to receive POST request from data center to centeralized server
"""


from flask import Flask, request, abort, Response
from flask_cors import CORS


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
        print('Interfaces:', interfaces)
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
    json = {'message': 'Success'}
    return Response(json, mimetype='application/json')


if __name__ == '__main__':
    # print("App is running in %s on port %s" % (config.env['ENVIRONMENT'], config.env['PORT']))
    # app.run(host=config.env['HOSTNAME'], port=config.env['PORT'])
    print("App is running")
    app.run()

app.config['DEBUG'] = True
