#importing necessary library
from flask_restful import Resource, reqparse
from flask import Response, request


#importing database code
import db


#creating class to get all users data
class getUserData(Resource):

	def get(self):					#method for get
		get_data=db.get_data()
		return get_data



#class to post user data
class postUserData(Resource):

	def post(self):					#method for post
		data={
		'username': request.args.get('username'),
		'email': request.args.get('email'),
		'password': request.args.get('password')
		}
		post_data=db.insert_data(data)
		return post_data



#class for get, post, delete command which requires id 
class userDataId(Resource):

	def get(self, id):							#method for get using id
		get_data=db.get_data_by_id(id)
		return Response(get_data, mimetype="application/json")

	def put(self, id):							#method for put using id
		data={'email': 'kripesh@gmail.com'}
		put_data=db.update_data(id, data)
		return Response(put_data, mimetype="application/json")

	def delete(self, id):						#method for delete using id
		delete_data=db.delete_data(id)
		return Response(delete_data, mimetype="application/json")
