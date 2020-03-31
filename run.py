import os

from app import create_app
from app.db import db

config_name = os.environ.get('CONFIG_NAME')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()