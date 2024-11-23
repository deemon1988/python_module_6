import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Example with Sprite"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_sprite = None

    def setup(self):
        """Инициализация игры"""
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        """Рисует содержимое окна"""
        self.clear()
        self.player_sprite.draw()

    def on_update(self, delta_time):
        """Обновляет состояние игры"""
        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y
        if self.player_sprite.right >= SCREEN_WIDTH:
            self.player_sprite.right = SCREEN_WIDTH
        if self.player_sprite.left <= 0:
            self.player_sprite.left = 0
        if self.player_sprite.top >= SCREEN_HEIGHT:
            self.player_sprite.right = SCREEN_HEIGHT
        if self.player_sprite.bottom <= 0:
            self.player_sprite.bottom = 0


    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        if key == arcade.key.UP:
            self.player_sprite.change_y = 5
        if key == arcade.key.DOWN:
            self.player_sprite.change_y = -5

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()

