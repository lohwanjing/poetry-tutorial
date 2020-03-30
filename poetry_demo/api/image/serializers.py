from flask_restplus import fields
from rest_api_demo.api.restplus import api

person = api.model('Person', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a person'),
    'name': fields.String(description='Name of person'),
    'gender': fields.String(description='Gender'),
    'dob': fields.DateTime(description='Date of Birth'),
})

image = api.model('Account', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a image'),
    'description': fields.String(required=True, description='Description of image'),
    'source': fields.String(required=True, description='Source url of image'),
    'tagged': fields.List(fields.Nested(person))
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})
