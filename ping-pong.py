import random

import arcade

from space_invaders import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ping Pong"


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.14)
        self.change_x = -3.5
        self.change_y = 3.5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        elif self.left <= 0:
            self.change_x = -self.change_x
        elif self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        elif self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.35)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def update(self, delta):
        self.ball.update()
        self.bar.update()

        # Избегание застревания
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
            self.ball.change_x += random.uniform(-0.5, 0.5)  # Добавляем случайное смещение
            # Исправляем положение мяча
            if self.ball.center_y > self.bar.center_y:
                self.ball.bottom = self.bar.top + 0.01
            elif self.ball.center_y < self.bar.center_y:
                self.ball.top = self.bar.bottom - 0.01

            # Проверяем, где произошло столкновение
            if self.ball.center_y > self.bar.center_y:  # Мяч сверху
                self.ball.change_y = abs(self.ball.change_y)  # Движение вверх
            elif self.ball.center_y < self.bar.center_y:  # Мяч снизу
                self.ball.change_y = -abs(self.ball.change_y)  # Движение вниз
            # Дополнительно проверяем боковое столкновение
            if self.ball.center_x > self.bar.center_x or self.ball.center_x < self.bar.center_x:
                self.ball.change_x = -self.ball.change_x

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 1.1

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()


if __name__ == "__main__":
    windows = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
