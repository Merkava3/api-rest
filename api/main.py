import sys
from os.path import abspath, dirname

sys.path.append(dirname(abspath(__file__)))

from app import create_app
from config import Config

enviroment = Config['development']

app = create_app(enviroment)

if __name__ == '__main__':
    app.run()