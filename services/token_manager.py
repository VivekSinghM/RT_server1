from datetime import datetime,timedelta
import jwt

class Token:
    
    @staticmethod
    def get_token(public_id,exp_time,app_secret_key):
        return jwt.encode({
            'public_id': public_id,
            'exp': datetime.utcnow() + timedelta(minutes = exp_time)
        }, app_secret_key)
    
    @staticmethod
    def check_token(token, app_secret_key):
        data = jwt.decode(token, app_secret_key)
        public_id = data['public_id']
        user=""
        return user

