# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes, about_routes
from web_app.routes.model_routes import model_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(model_routes)
    app.register_blueprint(about_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)