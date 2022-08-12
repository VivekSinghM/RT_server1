# from flask import Flask, request, jsonify
# from constant import *
# from services.token_manager import Token

# app = Flask(__name__)
# app.secret_key = secret_key


# def auth_token_required(func):
#     @warps(func)
#     def decorated(*args,**kargs):
#         _token= None
#         if '_token' in request.headers:
#             _token = request.headers['_token']
#         if not _token:
#             return jsonify({"message": "no token found"}), 401
#         try:
#             user = Token.check_token(_token, app.secret_key)
#         except:
#             return jsonify({'message': "token invalid! :( "}), 401
#         return func (user, *args, **kargs)
#     return decorated

# from flask import Flask, request, jsonify
# from constant import *
# from services.token_manager import Token

# app = Flask(__name__)
# app.secret_key = secret_key

# import api.all_api_call
# if __name__ == '__main__':
#     app.run(debug=True)

