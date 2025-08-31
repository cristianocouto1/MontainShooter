from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        # Chama o construtor da classe pai
        super().__init__(name, position)
        self.is_alive = True

    def move(self):
        # Move o tiro do jogador para a direita
        self.rect.centerx += ENTITY_SPEED[self.name]