import socket
from enum import Enum, auto


class ServerState(Enum):
    WAITING = auto()
    CONNECTED = auto()
    DISCONNECTED = auto()


class Server:
    HOST = '127.0.0.1'
    PORT = 8000

    def __init__(self):
        self.state = ServerState.WAITING
        self.connections: list[tuple[socket.socket, any]] = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((Server.HOST, Server.PORT))
        self.socket.listen(10)
        print("Server started, waiting for connection")

        while True:  # State Machine
            if self.state is ServerState.WAITING:
                self.wait_for_connection()  # what if message while waiting?
                if len(self.connections) == 2:
                    self.state = ServerState.CONNECTED
                    print("Server is connected to two clients")
            elif self.state is ServerState.CONNECTED:
                for conn, addr in self.connections:
                    self.wait_for_message(conn, addr)

    def wait_for_connection(self):
        conn, addr = self.socket.accept()  # waits until get connection request
        server_message = 'You connected to the server!'
        conn.sendto(server_message.encode(), addr)
        print(f"Connected to client at address: {addr}")
        self.connections.append((conn, addr))

    def wait_for_message(self, conn: socket.socket, addr: any):
        try:
            client_message = str(conn.recv(1024), encoding='utf-8')
            print('Client message is:', client_message, "from:", addr)
            server_message = 'The server got your message!'
            conn.sendto(server_message.encode(), addr)
        except ConnectionResetError:
            print("lost connection")
            conn.close()
            self.connections.remove((conn, addr))
            self.state = ServerState.WAITING
            print("Server lost a connection, waiting for reconnect")
        except Exception as e:
            print(f"got some other error {e}")
            exit()


if __name__ == "__main__":
    server = Server()
