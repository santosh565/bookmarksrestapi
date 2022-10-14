from flask import Flask


def create_app():
    app = Flask(__name__)
    
    @app.get('/')
    def get_admin():
        return 'hello'
    
    return app
    
    