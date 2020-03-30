import logging

from flask import request
from flask-restplus import Resource
from poetry_demo.api.image.business import create_person, update_person, delete_person
from poetry_demo.api.image.serializers import person
from poetry_demo.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('image/persons', description='Operations related to people found in images')


@ns.route('/')
class PersonCollection(Resource):

    @api.marshal_list_with(person)
    def get(self):
        """
        Returns list of persons
        """
        data = [
            {"id": 1, "name": "Alice", "gender": "F", "dob": "2000-09-28"},
            {"id": 2, "name": "Bob", "gender": "M", "dob": "2000-09-28"},
            {"id": 3, "name": "Charlie", "gender": "M", "dob": "2000-09-28"}
        ]
        return data

    @api.response(201, 'Person successfully created.')
    @api.expect(person)
    def post(self):
        """
        Creates a person
        """
        data = request.json
        create_person(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Person not found.')
class PersonItem(Resource):

    @api.marshal_with(person)
    def get(self, id):
        """
        Returns a category with a list of posts.
        """
        data = {"id": 1, "name": "Alice", "gender": "F", "dob": "2000-09-28"}
        return data

    @api.expect(person)
    @api.response(204, 'Category successfully updated.')
    def put(self, id):
        """
        Updates a person.
        Use this method to change the name of a blog category.
        * Send a JSON object with the new data in the request body.
        """
        data = request.json
        update_person(id, data)
        return None, 204

    @api.response(204, 'Category successfully deleted.')
    def delete(self, id):
        """
        Deletes person
        """
        delete_person(id)
        return None, 204
