from flask import Blueprint, jsonify, request


api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'mesaje': "hola mundo"})

@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    pass

@api_v1.route('/tasks', methods=['POST'])
def create_task():
    pass

@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    pass
    
@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    pass

    