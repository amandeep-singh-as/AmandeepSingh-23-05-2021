This project is based on Python, Flask framework and SQLite DB.

A simple web based project for user reistration, login and log out functionality.

Files and directories
    index.py = Main application file
    
    config.py = Configration class file

    app.db = SQLite database file.

    .flaskenv = Flask env file

    venv = Python virtual environment directory

    migration = Flask DB migration files

    app = main app directory
        routes = Handles all the routes and bussiness logic

        models = data models

        templates = HTML based templates for UI in this dir

        __init__.py = package file



Running the app:
    1. Open cmd / teminal
    2. Go to venv -> Scripts -> activate
        Windows:
            cd venv/Scripts
            activate
    3. Go back to home directory
    4. Run
        Flask run
    5. Open browser 
        localhost:5000

TEST CASES:
    username : johndoe@test.com
    password : johndoe

    username : jamesbond@007.com
    password : jamesbond007