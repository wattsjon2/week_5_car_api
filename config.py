import os

basedir = os.path.abspath(os.path.dirname(__file__))

# give access to the project in ANY OS we find ourselves in
# Aloow outside files/folders to be added to  the project
# base directory

class Config():
    """
        Set Config variables for the flask app
        using Enviorment variables where available
        create config variables if not done already
    
    """
    SECRECT_KEY = os.environ.get('SECRECT_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # turn off messages for updates in sqlalchemy