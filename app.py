# from main import app
# import api.all_api_call

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
from constant import *
from services.token_manager import Token

app = Flask(__name__)
app.secret_key = secret_key
CORS(app)
cors=CORS(app,resources={
    r"/*":{
        "origins":"*"
    }
})

import api.authentication
import api.table_manager
import api.menu_manger
from api.all_api_call import app

if __name__ == '__main__':
    app.run(debug=True)
