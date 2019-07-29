import bottle
import json

from bottle import request, response, route, get, post, abort, HTTPResponse

CONTACTS = [
        {
            "id": 1,
            "name": "Matthew",
            "phone": "356789"
        },

        {
            "id": 2,
            "name": "John",
            "phone": "132538"
        },

        {
            "id": 3,
            "name": "Smith",
            "phone": "583486"
        }
]


@get('/')
def index():
    response.headers['Content-Type'] = 'application/json'

    return json.dumps(CONTACTS)

@get('/<contact_id:int>')
def show(contact_id):
    found = list(filter(lambda x: x['id'] == contact_id, CONTACTS))
    response.headers['Content-Type'] = 'application/json'
    if len(found) == 0:
        return HTTPResponse(
            status=404,
            body=json.dumps({'Error': "Not found"})
        )
    else:
        return json.dumps(found[0])


@post('/')
def create():
    new_contact = request.json
    return HTTPResponse(
        status=201,
        body=json.dumps(new_contact),
        headers={'Content-Type': 'application/json'}
    )

@route('/<contact_id:int>', method='PUT')
def update(contact_id):
    found = list(filter(lambda x: x['id'] == contact_id, CONTACTS))
    if len(found) == 0:
        return HTTPResponse(
            status=404,
            body=json.dumps({'Error': "Not found"})
        )
    params = request.json
    print(params)
    updated = {**found[0], **params}
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(updated)


@route('/<contact_id:int>', method="DELETE")
def delate(contact_id):
    found = list(filter(lambda x: x['id'] == contact_id, CONTACTS))
    response.headers['Content-Type'] = 'application/json'
    if len(found) == 0:
        return HTTPResponse(
            status=404,
            body=json.dumps({'Error': "Not found"})
        )
    else:
        return HTTPResponse(
            status=204
        )

