from flask import Blueprint, jsonify

from api.auth_manager import auth_blueprint
from api.table_manager import table_blueprint
from api.menu_manger import menu_blueprint

base_blueprint = Blueprint(name='base_routes',import_name=__name__)

@base_blueprint.route("/",methods=["GET","POST"])
def home_app():
    return jsonify({"app-working":True})

@base_blueprint.route("/checkApp",methods=["GET","POST"])
def chech_app():
    return jsonify({"app-working":True})