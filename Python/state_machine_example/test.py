from pycat.core import Window, Sprite, Color
from enum import Enum, auto

w = Window()


class MySprite(Sprite):

    class State(Enum):
        JUMPING = auto()
        FALLING = auto()
        WALKING = auto()

    def on_create(self):
        self.scale = 100
        self.color = Color.AMBER
        self.x = 100
        self.y = 100
        self.y_speed = 0
        self.state = MySprite.State.JUMPING

    def on_update(self, dt):
        if self.state is MySprite.State.JUMPING:
            if self.y_speed <= 0:
                self.state = MySprite.State.FALLING
        if self.state is MySprite.State.FALLING:
            if self.is_touching_ground():
                self.state = MySprite.State.WALKING
        elif self.state is MySprite.State.WALKING:
            if w.is_key_down(" "):
                self.state = MySprite.State.JUMPING
            elif not self.is_touching_ground():
                self.state = MySprite.State.FALLING

    def is_touching_ground(self):
        return False


sprite = w.create_sprite(MySprite)
w.run()
