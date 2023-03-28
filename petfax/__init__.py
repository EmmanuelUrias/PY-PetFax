from flask import Flask
from flask_migrate import Migrate


# factory
def create_app():
    app = Flask(__name__)

    #db config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:eu1208007!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, Petfax!'

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact_form
    app.register_blueprint(fact_form.bp)

    return app
