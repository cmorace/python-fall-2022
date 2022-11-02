from pycat.core import Window, Sprite, Color

w = Window(enforce_window_limits=False)


class Ship(Sprite):
    DR = 2
    DS = 0.15
    MAX_SPEED = 8

    def on_create(self):
        self.scale = 50
        self.color = Color.RED
        self.position = w.center
        self.speed = 0

    def on_update(self, dt):
        if w.is_key_pressed("a"):
            self.rotation += Ship.DR
        if w.is_key_pressed('d'):
            self.rotation -= Ship.DR
        if w.is_key_pressed('w'):
            self.speed += Ship.DS
            self.speed = min(self.speed, Ship.MAX_SPEED)
        if w.is_key_pressed('s'):
            self.speed -= Ship.DS
            self.speed = max(self.speed, 0)
        if w.is_key_down(' '):
            w.create_sprite(Bullet)

        self.move_forward(self.speed)
        if self.x > w.width:
            self.x = 0
        elif self.x < 0:
            self.x = w.width
        if self.y > w.height:
            self.y = 0
        elif self.y < 0:
            self.y = w.height


class Bullet(Sprite):

    def on_create(self):
        self.position = player.position
        self.rotation = player.rotation
        self.scale = 10

    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()


player = w.create_sprite(Ship)
w.run()
