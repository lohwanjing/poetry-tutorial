from flask_restful_swagger_2 import Schema


class PersonModel(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'integer',
            'format': 'int64',
        },
        'name': {
            'type': 'string',
        },
        'gender': {
            'type': 'string',
        },
        'dob': {
            'type': 'string',
            'format': 'date',
        },
    }
    required = ['name']


class ImageModel(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'integer',
            'format': 'int64',
        },
        'description': {
            'type': 'string',
        },
        'source': {
            'type': 'string',
            'format': 'url',
        },
        'tagged': {
            'type': PersonModel.array(),
        },
    }
