import socket
from pycat.core import Window, Sprite

HOST = '127.0.0.1'
PORT = 8000
clientMessage = 'Hello!'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

w = Window()


class Button(Sprite):

    def on_create(self):
        self.scale = 100
        self.position = w.center

    def on_left_click(self):
        
        client.sendall(clientMessage.encode())
        # serverMessage = str(client.recv(1024), encoding='utf-8')
        # print('Server:', serverMessage)


w.create_sprite(Button)
w.run()


# client.close()