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

{(response_body)}''' #Найти HTTP header


            connection.sendall(response.encode())



with socketserver.TCPServer(('', 5680), Handler) as server:
    server.allow_reuse_address = True
    server.serve_forever()