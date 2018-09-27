import sumTwoNumbers
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class sumNumbers(Resource):
    def get(self, question, response):
        return {'data': sumTwoNumbers.analysis_by_sentence(question,response)}

api.add_resource(sumNumbers, '/<question>/<response>/')

if __name__ == '__main__':
     app.run()