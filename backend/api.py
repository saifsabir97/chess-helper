import urllib.parse

from flask import Flask, request, Response

from backend.system.constants import EngineType, Platform
from backend.system.system import System

app = Flask(__name__)


@app.route('/getNextMove', methods=['POST'])
def get_next_move():
    # TODO: get engine preference from user directly
    engine_type = EngineType['stockfish']

    # get platform/website name
    parsed_url = urllib.parse.urlparse(request.headers.get("origin"))
    host_platform = parsed_url.hostname
    host_platform = host_platform.split(".")[-2]
    platform = Platform[host_platform]

    # create system instance
    system = System(engine_type, platform)

    # get html page data
    input_data = request.data

    # get result
    result = system.get_next_move(input_data)
    result = str({"next_move": result})

    response = Response(result, status=201, mimetype='application/json')
    response.headers.set("Access-Control-Allow-Origin", "*")
    response.headers.set("Access-Control-Allow-Headers", "Content-Type")
    response.headers.set("Content-Type", "application/json")
    return response


if __name__ == '__main__':
    app.run()
