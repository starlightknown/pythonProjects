import socket
CHUNK = 6435
port = 3000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostname = '127.0.0.1'
while True:
    s.connect((hostname,port))
    message = input("type message: ")
    data = message.encode('ascii')
    s.send(data)
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"karuna says:{text}")
