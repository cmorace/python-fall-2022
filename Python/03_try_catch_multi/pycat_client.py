import socket
from pycat.core import Window, Sprite

HOST = '127.0.0.1'
PORT = 8000
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
server_message = str(socket.recv(1024), encoding='utf-8')
print("Got ack from server:", server_message)
w = Window(200, 200)


class Button(Sprite):

    def on_create(self):
        self.scale = 100
        self.position = w.center

    def on_left_click(self):
        clientMessage = 'Hello Server!'
        socket.send(clientMessage.encode())
        server_message = str(socket.recv(1024), encoding='utf-8')
        print("Got ack from server:", server_message)


w.create_sprite(Button)
w.run()
