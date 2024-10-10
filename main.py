import threading

# import "packages" from flask
from flask import render_template,request  # import render_template from "public" flask libraries
from flask.cli import AppGroup
from flask_cors import CORS
import functools


# import "packages" from "this" project
from __init__ import app, db, cors  # Definitions initialization


# setup APIs
from api.user import user_api # Blueprint import api definition
from api.player import player_api
from api.song import Song_api
# database migrations
from model.users import initUsers
from model.players import initPlayers
from model.songs import initSongs



# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(user_api) # register api routes
app.register_blueprint(player_api)
app.register_blueprint(Song_api)
app.register_blueprint(app_projects) # register app pages

cors = CORS(app, resources={r"/api/*": {"origins": ["http://127.0.0.1:5500", "http://127.0.0.1:4100"]}})


@app.before_request
def before_request():
    initSongs()  # Keep the initialization, remove the CORS part



@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")



@app.route('/album/<album_name>')
def album(album_name):
    # Your code to fetch album details based on album_name from the backend
    # Example data for demonstration, replace this with actual data retrieval
    album_data = {
        'name': album_name,
        'description': 'Your album description here.',
        'songs': ['Song 1', 'Song 2', 'Song 3']  # Add actual song data
    }
    return render_template('album.html', album_data=album_data)


@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

def allow_origin(origin):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if origin in ['http://localhost:4100', 'http://127.0.0.1:4100', 'https://nighthawkcoders.github.io']:
                cors.add_allowed_origin(origin)
            return f(*args, **kwargs)
        return wrapper
    return decorator

# Create an AppGroup for custom commands
custom_cli = AppGroup('custom', help='Custom commands')

# Define a command to generate data
@custom_cli.command('generate_data')
def generate_data():
    initUsers()
    initPlayers()
    initSongs()


# Register the custom command group with the Flask application
app.cli.add_command(custom_cli)
        
# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    app.run(debug=True, host="0.0.0.0", port="8086")