# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

from db_accessors.project_metadata_accessor import ProjectMetadataDB
from db_accessors.project_progress_accessor import ProjectProgressDB
from db_accessors.project_scope_accessor import ProjectScopeDB
from models.project_metadata import ProjectMetadata
from models.project_progress import ProjectProgress
from models.project_scope import ProjectScope

app = Flask(__name__)
CORS(app)

# Initialize database accessors
project_metadata_db = ProjectMetadataDB('database.db')
project_scope_db = ProjectScopeDB('database.db')
project_progress_db = ProjectProgressDB('database.db')

# project_metadata endpoints
@app.route('/project_metadata', methods=['POST'])
def create_project():
    data = request.json
    project_metadata = ProjectMetadata(None, data['address'], data['owner'], data['phone'], data['status'], data['total_price'])
    project_metadata_id = project_metadata_db.create(project_metadata)
    return jsonify({'id': project_metadata_id}), 201

@app.route('/project_metadata/<int:project_metadata_id>', methods=['GET'])
def get_project(project_metadata_id):
    project_metadata = project_metadata_db.read(project_metadata_id)
    if project_metadata:
        return jsonify(project_metadata.__dict__)
    return jsonify({'error': 'project_metadata not found'}), 404

@app.route('/project_metadata/<int:project_metadata_id>', methods=['PUT'])
def update_project(project_metadata_id):
    data = request.json
    project_metadata = project_metadata_db.read(project_metadata_id)
    if project_metadata:
        project_metadata.address = data['address']
        project_metadata.owner = data['owner']
        project_metadata.phone = data['phone']
        project_metadata.status = data['status']
        project_metadata.total_price = data['total_price']
        project_metadata_db.update(project_metadata)
        return jsonify({'message': 'project_metadata updated'})
    return jsonify({'error': 'project_metadata not found'}), 404

@app.route('/project_metadata/<int:project_metadata_id>', methods=['DELETE'])
def delete_project(project_metadata_id):
    project_metadata = project_metadata_db.read(project_metadata_id)
    if project_metadata:
        project_metadata_db.delete(project_metadata_id)
        return jsonify({'message': 'project_metadata deleted'})
    return jsonify({'error': 'project_metadata not found'}), 404

@app.route('/projects', methods=['GET'])
def get_all_projects():
    projects = project_metadata_db.read_all()  # Assuming you have a method to read all projects
    return jsonify([project.__dict__ for project in projects])

# project_metadata Scope endpoints
@app.route('/project_scope', methods=['POST'])
def create_project_scope():
    data = request.json
    project_scope = ProjectScope(None, data['project_metadata_id'], data['scope'])
    scope_id = project_scope_db.create(project_scope)
    return jsonify({'id': scope_id}), 201

@app.route('/project_scope/<int:scope_id>', methods=['GET'])
def get_project_scope(scope_id):
    project_scope = project_scope_db.read(scope_id)
    if project_scope:
        return jsonify(project_scope.__dict__)
    return jsonify({'error': 'project_metadata scope not found'}), 404

@app.route('/project_scope/<int:scope_id>', methods=['PUT'])
def update_project_scope(scope_id):
    data = request.json
    project_scope = project_scope_db.read(scope_id)
    if project_scope:
        project_scope.project_metadata_id = data['project_metadata_id']
        project_scope.scope = data['scope']
        project_scope_db.update(project_scope)
        return jsonify({'message': 'project_metadata scope updated'})
    return jsonify({'error': 'project_metadata scope not found'}), 404

@app.route('/project_scope/<int:scope_id>', methods=['DELETE'])
def delete_project_scope(scope_id):
    project_scope = project_scope_db.read(scope_id)
    if project_scope:
        project_scope_db.delete(scope_id)
        return jsonify({'message': 'project_metadata scope deleted'})
    return jsonify({'error': 'project_metadata scope not found'}), 404

# project_metadata Progress endpoints
@app.route('/project_progress', methods=['POST'])
def create_project_progress():
    data = request.json
    project_progress = ProjectProgress(None, data['project_metadata_id'], data['work_done'], data['payment_percentage'], data['payment_value'])
    progress_id = project_progress_db.create(project_progress)
    return jsonify({'id': progress_id}), 201

@app.route('/project_progress/<int:progress_id>', methods=['GET'])
def get_project_progress(progress_id):
    project_progress = project_progress_db.read(progress_id)
    if project_progress:
        return jsonify(project_progress.__dict__)
    return jsonify({'error': 'project_metadata progress not found'}), 404

@app.route('/project_progress/<int:progress_id>', methods=['PUT'])
def update_project_progress(progress_id):
    data = request.json
    project_progress = project_progress_db.read(progress_id)
    if project_progress:
        project_progress.project_metadata_id = data['project_metadata_id']
        project_progress.work_done = data['work_done']
        project_progress.payment_percentage = data['payment_percentage']
        project_progress.payment_value = data['payment_value']
        project_progress_db.update(project_progress)
        return jsonify({'message': 'project_metadata progress updated'})
    return jsonify({'error': 'project_metadata progress not found'}), 404

@app.route('/project_progress/<int:progress_id>', methods=['DELETE'])
def delete_project_progress(progress_id):
    project_progress = project_progress_db.read(progress_id)
    if project_progress:
        project_progress_db.delete(progress_id)
        return jsonify({'message': 'project_metadata progress deleted'})
    return jsonify({'error': 'project_metadata progress not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
