from flask import Flask, request
from name_sq import get_name
from flask_utils import serialize_names

app = Flask(__name__)

@app.route('/getname', methods=['GET'])
def getname():
    id = request.args.get('id')
    names = get_name(id)

    for name in names:
        return serialize_names(name)
    return {}