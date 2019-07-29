import socketserver

class Handler(socketserver.BaseRequestHandler):
    def hendle(self):
        while True:
            connection = self.request

            msg = connection.recv(1024)
            print(msg.decode('utf-8'))

            response_body = '<h1>Hello</h1>'



            response = f'''
HTTP/1.1 200 OK
Content-Type; text/html
Content-Length: {len(response_body)}
Connection: keep-alive

{(response_body)}'''


            connection.sendall(response.encode())



with socketserver.TCPServer(('' , 8081), Handler) as server:
    server.allow_reuse_address = True
    server.serve_forever()


# import json

# #j = '{"text":"text","number":1.2, "Nano": null, "bool": true}'
# #j = '[1, 2, 3, 4, 5]'
# j = '[{"1":[1,1,1]}, {"2":{"2":2}}]'
# print(json.loads(j)[1]["2"]["2"])
#
# #============
# to_json = [{"1":1, "2": 2}]
# print(json.dumps(to_json)
# #=============


# import requests
# params = {'key1': 1, 'key2':2}
#
#
# r = requests.get('https://httpbin.org/get', params=params)
# print(t.text, r.url)
# #print(dir(r), type(r))