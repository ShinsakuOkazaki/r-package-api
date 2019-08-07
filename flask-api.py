from flask import Flask, request
from flask_restful import Resource, abort, Api
import datetime
from marshmallow import Schema, fields, pprint

app = Flask(__name__)

api = Api(app)

SUBMITS= {
    "studentEmail": "so4639@bu.edu",
    "hash": 123,
    "assignmentID": "Assignment3",
    "osType": "osX",
    "taskID": 1,
    "answer": 0.3,
    "grade": 0.5,
}

class SubmitShcema(Schema):
    studentEmail= fields.String()
    hash= fields.Integer()
    assignmentID = fields.String()
    osType = fields.String()
    taskID = fields.Integer()
    answer= fields.Float()
    grade= fields.Float()

class SubmitList(Resource):
    def post(self):
        json = request.data
        schema = SubmitShcema()
        content = schema.loads(json).data
        pprint(content)
        submit_id = str(datetime.datetime.now())
        new_submit = {
            "studentEmail": content["studentEmail"],
            "hash": content['hash'],
            "assignmentID": content["assignmentID"],
            "osType": content["osType"],
            "taskID": content["taskID"],
            "answer": content["answer"],
            "grade": content["grade"]
        }

        SUBMITS[submit_id] = new_submit
        result = schema.dumps(content)
        return result, 201

api.add_resource(SubmitList, '/submits')


if __name__ == '__main__':
    app.run(debug=True)