import socket
from enum import Enum, auto


class ServerState(Enum):
    WAITING = auto()
    CONNECTED = auto()
    DISCONNECTED = auto()


state = ServerState.WAITING

connections = []

HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
print("Server started, waiting for connection")

while True:
    if state is ServerState.WAITING:
        conn, addr = server.accept()  # wait until get a message
        server_message = 'connected to client'
        conn.sendall(server_message.encode())
        print("got connection")
        connections.append((conn, addr))
        if len(connections) == 2:
            state = ServerState.CONNECTED
    elif state is ServerState.CONNECTED:
        # need to receive messages from both clients
        # threads, async, or processes
        for conn, addr in connections:
            try:
                client_message = str(conn.recv(1024), encoding='utf-8')
                print('Client message is:', client_message)
                server_message = 'I\'m here!'
                conn.sendall(server_message.encode())
            except ConnectionResetError:
                print("lost connection")
                conn.close()
                connections.remove((conn, addr))
                if len(connections) < 2:
                    state = ServerState.WAITING
            except:
                print("got some other error")
                exit()
