from app.server import server as app
from app import nodes
from app.models.match import Match
from flask import abort, request, jsonify, g, url_for, make_response
from werkzeug.datastructures import MultiDict
from cassandra.cqlengine import connection

connection.setup(nodes, "cqlengine", protocol_version=3)

# @app.route('/api/users/<int:id>')
# def get_user_by_id(id):
#     user = User.query.get(id)
#     if not user:
#         abort(404)
#     return jsonify({'element': user.to_json()})


# @app.route('/api/users/<string:username>')
# def get_user_by_username(username):
#     user = User.query.filter_by(username=username).first()
#     if not user:
#         abort(404)
#     return jsonify({'element': user.to_json()})


@app.route('/api/matches')
def get_users():
    matches = Match.objects().all()
    return jsonify({'elements': [element.get_data() for element in matches]})
