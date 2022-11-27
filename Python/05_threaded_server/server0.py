import socket
from socket import socket as Socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 8000

# connections: list[Connection] = list()
socket = Socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(10)
print("Server started, waiting for connection")
is_waiting_for_connection = False


class Connection:
    def __init__(self, socket: Socket, addr: any):
        self.socket = socket
        self.address = addr
        self.is_waiting_for_message = False

    def wait_for_message(self):
        try:
            self.is_waiting_for_message = True
            print("waiting for new message from connection")
            client_message = str(self.socket.recv(1024), encoding='utf-8')
            self.is_waiting_for_message = False
            print('Client message is:', client_message, "from:", c.address)
            server_message = 'The server got your message!'
            self.socket.sendto(server_message.encode(), c.address)
        except ConnectionResetError:
            print("lost connection")
            self.socket.close()
            connections.remove(self)
            print("Server lost a connection to client:", self.address)
        except Exception as e:
            print(f"Server has some unknown error {e}")
            print("This should never happen!!!!!!!!!!!!!!!!!!!!!!!")
            exit()


connections: list[Connection] = []


def wait_for_connection():
    global is_waiting_for_connection
    is_waiting_for_connection = True
    conn, addr = socket.accept()
    print("new connection")
    server_message = 'You connected to the server!'
    conn.sendto(server_message.encode(), addr)
    connections.append(Connection(conn, addr))
    is_waiting_for_connection = False


while True:
    # print('server')
    if not is_waiting_for_connection:
        print('starting new thread to wait for connection')
        t = Thread(target=wait_for_connection)
        t.start()

    for c in connections:
        if not c.is_waiting_for_message:
            t = Thread(target=c.wait_for_message)
            t.start()
