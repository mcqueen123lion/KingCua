from flask import Flask
import mlab

from mongoengine import *
from flask_restful import reqparse, Resource, Api

import json

mlab.connect()

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


class KingCua(Document):
    name = StringField()
    nationality = StringField()
    dateOfBirth = StringField()
    jobs = StringField()
    height = IntField()
    websites = ListField(StringField())
    images = ListField(StringField())
    marriage = BooleanField()


parser = reqparse.RequestParser()
parser.add_argument("name", type = str, location = "json")
parser.add_argument("nationality", type = str, location = "json")
parser.add_argument("dateOfBirth", type = str, location = "json")
parser.add_argument("jobs", type = str, location = "json")
parser.add_argument("height", type = int, location = "json")
parser.add_argument("websites", type = list, location = "json")
parser.add_argument("images", type = list, location = "json")
parser.add_argument("marriage", type = bool, location = "json")


class KingCuaRes(Resource):
    def get(self):
        return mlab.list2json(KingCua.objects)

    def post(self):
        args = parser.parse_args()
        name = args["name"]
        nationality = args["nationality"]
        dateOfBirth = args["dateOfBirth"]
        jobs = args["jobs"]
        height = args["height"]
        websites = args["websites"]
        images = args["images"]
        marriage = args["marriage"]

        new_KingCua = KingCua()
        new_KingCua.name = name
        new_KingCua.nationality = nationality
        new_KingCua.dateOfBirth = dateOfBirth
        new_KingCua.jobs = jobs
        new_KingCua.height = height
        new_KingCua.websites = websites
        new_KingCua.images = images
        new_KingCua.marriage = marriage
        new_KingCua.save()

        return mlab.item2json(new_KingCua)

api.add_resource(KingCuaRes, "/api/kingcua")

if __name__ == '__main__':
    app.run()
