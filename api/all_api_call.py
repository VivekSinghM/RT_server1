from main import app
from flask import jsonify

import api.authentication
import api.table_manager
import api.menu_manger

@app.route("/",methods=["GET","POST"])
def home_app():
    return jsonify({"app-working":True})

@app.route("/checkApp",methods=["GET","POST"])
def chech_app():
    return jsonify({"app-working":True})