# from flask_restx import Resource, Namespace
# from celery_worker import create_celery

# celery = create_celery()

# Ainamespace = Namespace(
#     name="AI",
#     description="AI CRUD를 작성하기 위해 사용하는 API.",
# )

# @Ainamespace.route('/test')
# @Ainamespace.doc(responses={200: 'Success'})
# @Ainamespace.doc(responses={404: 'Failed'})
# class AIClass(Resource):
#     @celery.task()
#     def post():
#         print("HI")
#         return "SUCCESS"

#     def get(self):
#         # postrun()
#         AIClass.post.delay()

# def postrun():
#     AIClass.post.delay()

# 둘 중 하나에서 값ㅇ, 받아서
# 셀러리로 넘겨서 다시 리턴값으로

########
from distutils.command.build_scripts import first_line_re
from flask import request
from flask_restx import Resource, Namespace
from celery_worker import create_celery
from celery.result import AsyncResult
# import base64
# import boto3
# import pickle
import json

celery = create_celery()

Ainamespace = Namespace(
    name="AI",
    description="AI CRUD를 작성하기 위해 사용하는 API.",
)

@Ainamespace.route('/test')
@Ainamespace.doc(responses={200: 'Success'})
@Ainamespace.doc(responses={404: 'Failed'})
class AIClass(Resource):
    
    def get(self):
        first_num = request.args.get('first_num')
        second_num = request.args.get('second_num')
        result = test.delay(first_num, second_num)
        return result.ready()

@celery.task()
def test(first_num, second_num):
    print(first_num)
    print(second_num)
    # print(self.AsyncResult(self.request.id).state) # pending
    # print("failed", self.AsyncResult(self.request.id).failed()) 
    # print("get", self.AsyncResult(self.request.id).get())
    # print("ready", self.AsyncResult(self.request.id).ready())
    return int(first_num) + int(second_num)


