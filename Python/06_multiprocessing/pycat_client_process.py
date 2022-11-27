import multiprocessing 
from pycat.core import Window, Sprite


def create_client(x):
    import socket
    HOST = '127.0.0.1'
    PORT = 8000
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((HOST, PORT))
    server_message = str(socket.recv(1024), encoding='utf-8')
    print("Got ack from server:", server_message)
    w = Window(100, 500)
    w._window.set_location(x, 0)


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


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    for i in range(10):
        p = multiprocessing.Process(target=create_client, args=(i*100,))
        p.start()
