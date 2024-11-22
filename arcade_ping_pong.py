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
        self.player_sprite.center_x += 1  # Двигаем спрайт вправо

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()

