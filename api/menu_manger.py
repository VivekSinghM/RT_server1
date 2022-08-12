import json
from main import app
from models.menu_model import Menu, TempMenu
from flask import make_response, jsonify, request


@app.route('/getMenu', methods=['GET'])
def get_menu():
    print("hi")
    return make_response(jsonify(TempMenu.menu) ,201)

@app.route('/addMenuItems',methods=['GET'])
def add_menu_item():
    temp_items=json.load(request.data())
    Menu.add_menu_item(temp_items)
    return make_response('true',201)
