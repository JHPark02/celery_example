from flask_restx import Api
from app import create_app
from namespaces import Ainamespace

app = create_app()

api = Api(
    app,
    version='0.1',
    title="Silicon Project's API Server",
    description="PRP!",
    terms_url="/",
    contact="vivian0304@naver.com",
    license="MIT"
)

api.add_namespace(Ainamespace.Ainamespace, '/ai')

if __name__ == "__main__":
    app.run(debug = True, host = 'localhost', port = 8080)