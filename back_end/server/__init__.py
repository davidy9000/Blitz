from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello() :
        return "Hello World! Welcome to Blitz"
    
    return app
