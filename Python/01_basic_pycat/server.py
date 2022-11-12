import socket
HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
print("Server started, waiting for connection")
conn, addr = server.accept()  # wait until get a message
server_message = 'connected to client'
conn.sendall(server_message.encode())
print("got connection")

while True:
    try:
        client_message = str(conn.recv(1024), encoding='utf-8')
        print('Client message is:', client_message)
        server_message = 'I\'m here!'
        conn.sendall(server_message.encode())
    except ConnectionResetError:
        print("lost connection")
        conn.close()
    except:
        print("got some other error")
        
