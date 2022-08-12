# from main import app
# import api.all_api_call

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from constant import *
from services.token_manager import Token

app = Flask(__name__)
app.secret_key = secret_key

import api.authentication
import api.table_manager
import api.menu_manger
from api.all_api_call import app


if __name__ == '__main__':
    app.run(debug=True)
