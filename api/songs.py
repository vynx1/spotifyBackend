from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db

from model.songs import Song

Song_api = Blueprint('Song_Api', __name__, url_prefix="/api/song")

api = Api(Song_api)

class SongAPI(Resource):
    def get(self, song_id=None):  # Add song_id as a parameter with a default value of None
        if song_id is not None:
            song = Song.query.get(song_id)
            if song:
                return jsonify(song.to_dict())
            return {"error": "Song not found"}, 404

        # Handle the case when no song_id is provided, e.g., for the "/all" endpoint
        songs = Song.query.all()
        songs_data = [song.to_dict() for song in songs]
        return jsonify(songs_data)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("_name", type=str, required=True, help="Name is required")
        parser.add_argument("_description", type=str, required=True, help="Description is required")
        parser.add_argument("_uri", type=str, required=True, help="URI is required")
        parser.add_argument("_tokens", type=int, required=True, help="Tokens is required")
        args = parser.parse_args()

        new_song = Song(_name=args["_name"], _description=args["_description"], _uri=args["_uri"], _tokens=args["_tokens"])
        db.session.add(new_song)
        db.session.commit()

        return jsonify(new_song.to_dict()), 201

    def put(self, song_id):
        song = Song.query.get(song_id)
        if not song:
            return {"error": "Song not found"}, 404

        parser = reqparse.RequestParser()
        parser.add_argument("_name", type=str)
        parser.add_argument("_description", type=str)
        parser.add_argument("_uri", type=str)
        parser.add_argument("_tokens", type=int)
        args = parser.parse_args()

        if args["_name"]:
            song._name = args["_name"]
        if args["_description"]:
            song._description = args["_description"]
        if args["_uri"]:
            song._uri = args["_uri"]
        if args["_tokens"]:
            song._tokens = args["_tokens"]

        db.session.commit()

        return jsonify(song.to_dict())

    def delete(self, song_id):
        song = Song.query.get(song_id)
        if not song:
            return {"error": "Song not found"}, 404

        db.session.delete(song)
        db.session.commit()

        return {"message": "Song deleted successfully"}, 200

api.add_resource(SongAPI, '/<int:song_id>', '/all')
