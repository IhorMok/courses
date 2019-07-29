# Сделать виртуальную среду
try:
    import ujson
except ImportError:
    import json as json

import bottle

from bottle import request, response, route
from bottle import get, post

# ПЕРВЫЙ СПОСОБ
# @get ('/')
# def index():
#     return 'Hello'
#
#
# @post('/')
# def post_index():
#     data = request.data
#     return data
# ВТОРОЙ СПОСОБ
# route
@route('/')
def index():
    return 'Index page'


# @route('/', method='post' )
# def return_data():
#     return request.json


@route('/')
def get_name():
    response.headers['Content-Type'] = 'application/json'
    response.json({'text1': 'json'})
    # return ujson.dumps({'from_server': "hello"})



bottle.run(port=8040)


# d = []
#
# GET (/) [{'key1' : "value1", "key2": "value2"}]
# GET (/<key>) -> {'key': 'value'}
# POST (/) <- {'key': 'value'}
# PUT (/<key>) <- 'new value'
# DELETE(/<key>) ->{'key': 'value'}

# JSON


# GET ('/')            повертає весь словник (масив{}) {'key1':'value1'}, {'key2':'value2'}
# GET ('/<key>')       повертає значення по ключу(в формат json) {'key':'value'}
# POST ('/')           {'key':'value'} - для апдейту словника
# PUT ('/<key>')      стрінгою передає значення ключа для апдейту 'new_value'
# DELETE ('/<key>')   {'key':'value'} - до видалення з словнику