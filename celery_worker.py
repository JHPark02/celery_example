# from celery import Celery
# from app import create_app
# import pymongo

# def create_celery():
#     # app = create_app()

#     # app.config.update(
#     #     CELERY_BROKER_URL='redis://localhost:6379',
#     #     CELERY_RESULT_BACKEND='redis://localhost:6379'
#     # )

#     celery = Celery(
#         'task', broker = 'amqp://localhost:5672', result_backend = 'mongodb://localhost:27017/')
#     # celery.conf.update(app.config)
    
#     mongodb_backend_settings = {
#         'database': '',
#         'taskmeta_collection': 'my_taskmeta_collection',
#     }

#     return celery
from celery import Celery
from app import create_app

def create_celery():

    celery = Celery(
        'task',
        broker = 'amqp://localhost:5672',
        result_backend='mongodb://localhost:27017/',
        mongodb_backend_settings = {
            'database': 'celeryTest0721',
            'taskmeta_collection': 'my_collection'
        })
    
    return celery