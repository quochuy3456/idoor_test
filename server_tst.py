import urllib.parse
from flask import request, redirect, jsonify, render_template
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from flask_cors import CORS, cross_origin
from wtforms import StringField
import time
import base64
import sys
from flask_wtf.csrf import CSRFError
from flask import Flask


app = Flask(__name__,  template_folder='templates')
# app.config['WTF_CSRF_FIELD_NAME'] = 'csrf_token'
csrf = CSRFProtect(app)
# token = csrf._get_csrf_token()
app.config['SECRET_KEY'] = "Hgdjihfoidhfoisvjhosvjnovndj2423kj4j234"
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/cgi-bin/basic": {"origins": "*"}})


class tst_form(FlaskForm):
    token = StringField("Token: ")


@app.route('/cgi-bin/basic', methods=['POST', ])
# @csrf.exempt
def cgi_bin_basic():
    if request.method == 'POST':
        token = request.form
        print(token)
        return jsonify({"result": "Success", "token": token})


@app.route('/cgi-bin/test')
def handle_csrf_error():
    form = tst_form()
    return render_template('form2.html', form=form)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
