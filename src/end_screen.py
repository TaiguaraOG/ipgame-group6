import pygame
from .settings import *


class VictoryScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 60, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 30)

        # Tenta carregar imagem, se der erro usa fundo preto
        try:
            # Lembre-se: use / para funcionar no Mac
            self.bg = pygame.image.load('assets/screens/victory.png').convert()
            self.bg = pygame.transform.scale(self.bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
        except:
            self.bg = None

    def draw(self):
        # 1. Se tiver imagem, desenha ela
        if self.bg:
            self.screen.blit(self.bg, (0, 0))

        # 2. Se não tiver imagem, desenha fundo preto e texto
        else:
            self.screen.fill((0, 0, 0))  # Preto

            # Texto Grande
            texto_win = self.font.render("MISSÃO CUMPRIDA!", True, (255, 255, 0))  # Amarelo
            rect_win = texto_win.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 50))
            self.screen.blit(texto_win, rect_win)

            # Texto Pequeno
            texto_inst = self.small_font.render("Pressione ENTER para Sair", True, (255, 255, 255))
            rect_inst = texto_inst.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50))
            self.screen.blit(texto_inst, rect_inst)