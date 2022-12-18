from pycat.core import Window, Sprite, Color, Point
from enum import Enum, auto

w = Window()
GRAVITY = 60
JUMP_VELOCITY = 2500
WALK_VELOCITY = 100
WALK_FRICTION = 0.9
AIR_FRICTION = 0.995


class MySprite(Sprite):

    class State(Enum):
        JUMPING = auto()
        FALLING = auto()
        WALKING = auto()

    def on_create(self):
        self.scale = 30
        self.color = Color.AMBER
        self.velocity = Point(0, 0)
        self.state = MySprite.State.FALLING
        self.x = self.width/2
        self.y = self.height/2
        self.a = self.position

    def on_update(self, dt):
        self.update_state(dt)
        if self.position.x < 0 or self.position.x > w.width:
            self.velocity.x = 0
        self.position += self.velocity * dt
        if self.a != self.position:
            w.create_line(self.a.x, self.a.y, self.position.x, self.position.y)
        self.a = self.position

    def update_state(self, dt: float):
        match self.state:
            case MySprite.State.JUMPING:
                self.jump()
            case MySprite.State.FALLING:
                self.fall()
            case MySprite.State.WALKING:
                self.walk()
            case _:
                print("unknown state")

    def jump(self):
        self.in_air_update()
        if self.velocity.y <= 0:
            self.state = MySprite.State.FALLING

    def fall(self):
        self.in_air_update()
        if self.is_touching_ground():
            self.state = MySprite.State.WALKING

    def walk(self):
        self.on_left_right_keys(dV=WALK_VELOCITY)
        self.velocity.x *= WALK_FRICTION
        if w.is_key_down(" "):
            self.velocity.y = JUMP_VELOCITY
            self.state = MySprite.State.JUMPING
        elif not self.is_touching_ground():
            self.state = MySprite.State.FALLING

    def is_touching_ground(self):
        if self.y > self.height/2:
            return False
        self.y = self.height/2
        self.velocity.y = 0
        return True

    def on_left_right_keys(self, dV):
        if w.is_key_pressed("a"):
            self.velocity.x -= dV
        elif w.is_key_pressed("d"):
            self.velocity.x += dV

    def in_air_update(self):
        self.on_left_right_keys(dV=10)
        self.velocity.y -= GRAVITY
        self.velocity *= AIR_FRICTION


sprite = w.create_sprite(MySprite)
w.run()
