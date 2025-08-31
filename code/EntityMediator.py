from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        # Verifica se a entidade saiu da tela
        if isinstance(ent, (Enemy, EnemyShot)):
            if ent.rect.right <= 0:
                ent.is_alive = False
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.is_alive = False

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        # Verifica a colisão entre duas entidades
        if (isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot)) or \
           (isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy)) or \
           (isinstance(ent1, Player) and isinstance(ent2, EnemyShot)) or \
           (isinstance(ent1, EnemyShot) and isinstance(ent2, Player)):
            if ent1.rect.colliderect(ent2.rect):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        # Adiciona pontos ao jogador que derrotou o inimigo
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # Itera sobre a lista para verificar colisões
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Marca entidades com vida zero como mortas
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                ent.is_alive = False