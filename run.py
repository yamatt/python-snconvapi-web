""" StatusNet Conversation API
    Copyright (C) 2011  Matt (yaMatt) Copperwaite

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask, render_template, Response, request
from Conversation import Conversation
try:
  import json    #python2.6
except ImportError:
  import simplejson as json #python2.5

app = Flask(__name__)

def jsoniffy (dictionary, jsonp=None):
  if jsonp:
    return "%s(%s)" % (jsonp, json.dumps(dictionary))
  else:
    return json.dumps(dictionary)

@app.route("/")
def index():
  return render_template('index.html')
    
@app.route("/<path:url>")
def get_conversation_data(url):
  if not url == "favicon.ico":
    conv = Conversation(url.encode())
    callback = request.args.get('callback', None)
    # I didn't like the Flask supplied jsonify function, I will propose a patch to work more like this
    if callback:
      return Response("%s(%s)" % (callback, json.dumps(conv.simple)), mimetype="application/json")
    else:
      return Response(json.dumps(conv.simple), mimetype="application/json")
  else:
    return "Doesn't have one", 404

if __name__ == "__main__":
    app.run(debug=True)
