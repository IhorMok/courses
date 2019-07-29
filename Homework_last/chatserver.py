import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ip = ""
# port = 8566
sock.bind(('127.0.0.1', 9050))
# sock.bind((ip), (port))
client = []
print("Start server")

while 1:
    data, addres = sock.recvfrom(1024)
    print(addres[0])
    if addres not in client:
        client.append(addres)
    for clients in client:
        if clients == addres:
            continue
        sock.sendto(data, clients)

























