from app import create_app
from config import Config

enviroment = Config['development']

app = create_app(enviroment)

if __name__ == '__main__':
    app.run()