import socket
from threading import Thread

socket.socket
class Connection:
    def __init__(self, socket: socket.socket, addr: any):
        self.socket = socket
        self.address = addr
        self.is_waiting_for_message = False

class Server:
    HOST = '127.0.0.1'
    PORT = 8000

    def __init__(self):
        self.connections: list[Connection] = list()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((Server.HOST, Server.PORT))
        self.socket.listen(10)
        print("Server started, waiting for connection")
        self.is_waiting_for_connection = False
        while True:
            print("server")
            for c in self.connections:
                if not c.is_waiting_for_message:
                    print("[NEW THREAD] wait_for_new_message")
                    t = Thread(target=self.wait_for_new_message, args=[c])
                    t.start()
                    print("after wait new message")
            if not self.is_waiting_for_connection:
                self.is_waiting_for_connection = True
                print("[NEW THREAD] wait_for_new_connection")
                t = Thread(target=self.wait_for_new_connection)
                t.start()

    def wait_for_new_connection(self):
        conn, addr = self.socket.accept()  # waits until get connection request
        self.is_waiting_for_connection = False
        server_message = 'You connected to the server!'
        conn.sendto(server_message.encode(), addr)
        print(f"Server has new connection at address: {addr}")
        c = Connection(conn, addr)
        self.connections.append(c)

    def wait_for_new_message(self, c: Connection):
        try:
            c.is_waiting_for_message = True
            print("waiting for new message from connection")
            client_message = str(c.socket.recv(1024), encoding='utf-8')
            c.is_waiting_for_message = False
            print('Client message is:', client_message, "from:", c.address)
            server_message = 'The server got your message!'
            c.socket.sendto(server_message.encode(), c.address)
        except ConnectionResetError:
            print("lost connection")
            c.socket.close()
            self.connections.remove(c)
            print("Server lost a connection to client at address:", c.address)
        except Exception as e:
            print(f"Server has some unknown error {e}")
            print("This should never happen!!!!!!!!!!!!!!!!!!!!!!!")
            exit()


if __name__ == "__main__":
    server = Server()
