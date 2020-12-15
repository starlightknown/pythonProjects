import socket
CHUNK = 6535
port = 3000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#create a socket object
#AF_NET:family of ipv4 ip address
hostname = '127.0.01' #ip address of local machines
s.bind((hostname,port))
print(f"server is live on {s.getsockname()}")
while True:
    data, clientAdd = s.recvfrom (CHUNK)
    message = data.decode('ascii')

    print("arya at{clientAdd}says:{message}")
    message_send = input("reply: ")
    data = message_send.encode('ascii')
    s.sendto(data,clientAdd)
