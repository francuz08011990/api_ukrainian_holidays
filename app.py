import settings

from flask import Flask
from flask_restful import Api

from urls import urls_v1


app = Flask(__name__)
api = Api(app)


for url_data in urls_v1:
    handler, url = url_data
    api.add_resource(handler, f'/api/v1/{url}')


if __name__ == '__main__':
    app.run(debug=settings.debug)
