import arcade

from arcade_ping_pong import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ping Pong"


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.25)
        self.change_x = 0.5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.3)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def update(self, delta):
        self.ball.update()


    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 1.1

    def on_draw(self):
        self.clear((255,255,255))
        self.bar.draw()
        self.ball.draw()



if __name__ == "__main__":
        windows = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.run()