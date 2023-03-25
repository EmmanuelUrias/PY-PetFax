from flask import Flask


# factory
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, Petfax!'

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact_form
    app.register_blueprint(fact_form.bp)

    return app
