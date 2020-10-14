import flask
from flask import request, jsonify
import json
import myserver.my as my
import myserver.converttojson as ctj

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>My4Server</h1>
<p>Welcome! Current version Beta 1.0.</p>'''

@app.route('/api/v1', methods=['GET'])
def apiV1():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'text' in request.args:
        text = request.args['text']
    else:
        jsonreturn = {
            "server":"OK",
            "api":"Data missing",
            "tosay":""
        }
        return json.dumps(jsonreturn)

    # Create an empty list for our results
    mytext = my.MyMain(text)

    myreturnjson = ctj.returntojson(mytext)
    return myreturnjson

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    # return jsonify(results)

## My imports
