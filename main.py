from flask import Flask
from flask import request
from flask import jsonify
from flask import request
#from flask_restful import Resource, Api, reqparse
from json import dumps
#from flask.ext.jsonpify import jsonify
import evals

app = Flask(__name__)
# api = Api(app)

# class Bot(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument("question")
#         args = parser.parse_args()
#         ans = evals.get_answer(args["question"])
#         return {'answer': ans} 


# api.add_resource(Bot, '/salesman') # Route_1

# if __name__ == '__main__':
#      app.run(port='5002')
     


#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument("question")
#         args = parser.parse_args()
#         ans = evals.get_answer(args["question"])
#         return {'answer': ans} 


@app.route('/salesman', methods=['post'])
def request_answer():
    qst = request.values['question']
    ans = evals.get_answer(qst)
    return jsonify({'answer': ans})

if __name__ == '__main__':
     app.run(port='8080')
