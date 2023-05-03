#importing necessary library
from flask import Flask
from flask_restful import Api
from api import getUserData, userDataId, postUserData


app = Flask(__name__)		#creating object for flask
api = Api(app)				#creating object for API



#adding api methods
api.add_resource(getUserData, '/users')
api.add_resource(userDataId, '/users/<id>')
api.add_resource(postUserData, '/users')




if __name__ == '__main__':
	app.run(debug=True)