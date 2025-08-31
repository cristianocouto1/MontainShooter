#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        # Inicializa o Pygame e a tela do jogo
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            # Inicia o jogo com base na opção do menu
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # Cria a lista de placares dos jogadores
                player_score = [0, 0]

                # Inicia o Nível 1
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                # Se o nível 1 for completado, inicia o Nível 2
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

                    # Se o nível 2 for completado, salva o placar
                    if level_return:
                        score.save(menu_return, player_score)

            # Mostra o placar
            elif menu_return == MENU_OPTION[3]:
                score.show()

            # Sai do jogo
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                sys.exit()

            # Sai do jogo se a opção for desconhecida
            else:
                pygame.quit()
                sys.exit()