import json

from flask import Flask, request, Response
from flask_cors import CORS

from database import DataBase

# Initial Store
store = DataBase()

# Initial App
app = Flask(__name__)
CORS(app)


# Home routes
@app.route('/')
def hello():
    return 'Welcome to My Flask RestAPI'


# GET - all items
@app.route('/tasks')
def get_all():
    data = store.get_all()
    return Response(json.dumps(data), mimetype='application/json')


# GET - single item
@app.route('/tasks/<item_id>')
def get_item(item_id):
    task = store.get(int(item_id))
    return Response(json.dumps(task), mimetype="application/json", status=200)


# POST - add new item
@app.route('/tasks', methods=['POST'])
def add_item():
    task = request.json['task']
    try:
        item = store.add(task)
        return {
                   'success': True,
                   'data': item,
                   'message': "Your item has been added successfully!"}, 200
    except:
        return {
                   'success': False,
                   'message': "The item already exists!"
               }, 409


@app.route('/tasks/<item_id>', methods=['PUT'])
def update_item(item_id):
    task = request.json
    store.update(task, int(item_id))
    return {
               'success': True,
               'data': task,
               'message': "Your item has been updated successfully!"}, 200


@app.route('/tasks/<item_id>/status', methods=['PUT'])
def update_item_status(item_id):
    status = request.json['status']
    store.update_field('status', status, int(item_id))
    return {
               'success': True,
               'message': "Your item has been updated successfully!"}, 200


# DELETE - delete item by id
@app.route('/tasks/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    store.delete(int(item_id))
    return {'success': True}, 200


app.run(host='0.0.0.0', port=8080)
