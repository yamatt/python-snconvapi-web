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

from flask import Flask, render_template, jsonify
from Conversation import Conversation
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')
    
@app.route("/<path:url>")
def get_conversation_data(url):
  conv = Conversation(url.encode())
  #annoyingly I have to declare it, I can't seen to use an anonymous dict
  #even though it wraps it in an anonymous dict
  return jsonify(result=conv.simple)

if __name__ == "__main__":
    app.run(debug=True)