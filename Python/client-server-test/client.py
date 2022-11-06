from pycat.core import Window, Sprite

w = Window()


class Button(Sprite):
    def on_create(self):
        self.width = 100
        self.height = 100
        self.position = w.center

    def on_left_click(self):
        # send msg to server
        print("I'm client, sending a msg to the server")


w.create_sprite(Button)
w.run()
