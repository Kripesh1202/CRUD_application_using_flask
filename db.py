#importing necessary library
from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient("mongodb://localhost:27017/")		#creating object for mongodb
db = client.user_data									#creating object for database
coll = db.data 											#creating object for collection



#inserting object to database
def insert_data(data):
	insert=coll.insert_one(data)
	return '{"message": "Inserted successful"}'


#getting data from the database using user id
def get_data_by_id(id):
	userdata=list(coll.find({'_id': ObjectId(id)}))
	if userdata is None:
		return {'message': 'No data found'}
	return userdata[0]['username']
		


#getting all username from database
def get_data():
	dusernames=[i for i in coll.find({}, {'_id': 0,'username': 1})]
	username=[j['username'] for j in dusernames]
	if username is None:
		return f"{'message': 'No data found'}"
	return jsonify(username)



#deleting data from database using user id
def delete_data(id):
	delete=coll.delete_one({'_id': ObjectId(id)})
	return "{'message': 'Deleted'}"



#updating data using user id
def update_data(id, data):
	uid = {'_id': ObjectId(id)}
	newValue = {'$set': data}
	update = coll.update_one(uid, newValue)
	return "{'message': 'Updated'}"




	