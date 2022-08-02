from flask_restful import Resource, reqparse
from flask import request
from models.user import UserModel
import time

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="Every user needs a email."
                        )
    parser.add_argument('password',
                    type=str,
                    required=True,
                    help="Every user needs a password."
                    )
    parser.add_argument('created_at',
                        type=time,
                        required=False,
                        )
    parser.add_argument('updated_at',
                        type=time,
                        required=False,
                        )


    def get(self, name):
        user = UserModel.find_by_name(name)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def post(self, name):
        if UserModel.find_by_name(name):
            return {'message': "An user with name '{}' already exists.".format(name)}, 400

        data = User.parser.parse_args()

        user = UserModel(name, **data)

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return user.json(), 201

    def delete(self, name):
        user = UserModel.find_by_name(name)
        if user:
            user.delete_from_db()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404

    def put(self, name):
        data = user.parser.parse_args()

        user = UserModel.find_by_name(name)

        if user:
            user.name = data['name']
        else:
            user = UserModel(name, **data)

        user.save_to_db()

        return user.json()


class UserList(Resource):
    def get(self):
        return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}

    def post(self):
        if UserModel.find_by_name(name):
            return {'message': "An user with name '{}' already exists.".format(name)}, 400

        data = User.parser.parse_args()

        user = UserModel(name, **data)

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return user.json(), 201
