from pycat.core import Window, Sprite, Color

w = Window()


class MySprite(Sprite):
    def on_create(self):
        self.scale = 100
        self.color = Color.AMBER
        self.x = 100
        self.y = 100
        self.y_speed = 0

    def on_update(self, dt):
        self.y_speed -= 1
        self.y += self.y_speed

        if w.is_key_down(" "):
            self.y_speed = 30


sprite = w.create_sprite(MySprite)
w.run()
