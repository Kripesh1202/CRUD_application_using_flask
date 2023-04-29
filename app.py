
#importing all necessary libraries
from flask import Flask, render_template, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId


#creating an flask object
app = Flask(__name__)

#creating an object for mongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.user_data
col = db.data


#route for GET command
@app.route('/users', methods=['GET'])
@app.route('/users/<id>', methods=['GET'])
#Function to display usernames
def read(id=None):
	#Displays specific user's username when id is provided
	if id is not None:
		userdata=list(col.find({'_id': ObjectId(id)}))
		if userdata is None:
			return "Error in displaying"
		return userdata[0]['username']
	#Diplay all username from Database
	else:
		dusernames=[i for i in col.find({}, {'_id': 0,'username': 1})]
		username=[j['username'] for j in dusernames]
		if username is None:
			return "Error in displaying"
		return username


#route for POST command
@app.route('/users/<username>+<email>+<password>', methods=['POST'])		#get data's from http request
def create(username,email,password):
	#make data to json format
	data={
	'username': username,           
	'email': email,	               
	'password': password  	  
	}
	insert=col.insert_one(data)			   #insert the data to database
	if insert:
		return "Inserted successfully"
	else:
		return "Error in insertion"


#route for PUT command
@app.route('/users/<id>', methods=['PUT'])
def update(id=None):
	uid = {'_id': ObjectId(id)}
	newValue = {'$set': {'email': 'temp@gmail.com'}}		#command to update data
	update = col.update_one(uid, newValue)
	if update.modified_count>0:
		return "Updated successfully"
	else:
		return "Error in updating"


#route for DELETE command
@app.route('/users/<id>', methods=['DELETE'])
def delete(id=None):
	dc=col.delete_one({'_id': ObjectId(id)})		#command to delete an element
	if dc:											#to check if userdata is deleted successfully
		return "Deleted successfully"
	else:
		return "Error in Deletion"


if __name__ == '__main__':
	app.run(debug=True)