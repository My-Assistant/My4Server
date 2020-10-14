import json

def returntojson(text):
    jsonreturn = {
        "server":"OK",
        "api":"OK",
        "tosay":text
    }
    return json.dumps(jsonreturn)
