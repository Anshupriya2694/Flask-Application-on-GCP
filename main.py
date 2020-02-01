# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import jsonify
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'This is a dictionary application. Send get request to server with the required word. \n Example: localhost/test will return the meaning of the word test'

@app.route('/<word>')
def search(word):
    word = word.lower()
    if word in data:
        return jsonify(data[word])
    elif word.title() in data:
        return jsonify(data[word.title()])
    elif word.upper() in data:
        return jsonify(data[word.upper()])
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean " + get_close_matches(word, data.keys())[0] + " instead?"
    else:
        return "Word doesn't exist"


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
