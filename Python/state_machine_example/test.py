from pycat.core import Window, Sprite, Color
from enum import Enum, auto

w = Window()


class MySprite(Sprite):

    class State(Enum):
        JUMPING = auto()
        WALKING = auto()

    def on_create(self):
        self.scale = 100
        self.color = Color.AMBER
        self.x = 100
        self.y = 100
        self.y_speed = 0
        self.state = MySprite.State.JUMPING

    def on_update(self, dt):
        if self.state == MySprite.State.JUMPING:
            pass
            if self.is_touching_ground():
                self.state = MySprite.State.WALKING
        elif self.state == MySprite.State.WALKING:
            pass
            if w.is_key_down(" "):
                self.state = MySprite.State.JUMPING

    def is_touching_ground(self):
        return False


sprite = w.create_sprite(MySprite)
w.run()
