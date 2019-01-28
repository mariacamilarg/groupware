import os

from flask import Flask
#from . import db
import db
#from . import auth, board
import auth
import board

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'keepcode.sqlite'),
    # )
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='../instance/keepcode.sqlite',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize database
    db.init_app(app)

    # register authentication blueprint
    app.register_blueprint(auth.bp)

    # register board blueprint
    app.register_blueprint(board.bp)
    app.add_url_rule('/', endpoint='index')

    return app

app = create_app()
#app.run()
