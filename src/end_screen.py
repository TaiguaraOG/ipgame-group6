import pygame


class VictoryScreen:
    def __init__(self, screen):
        self.screen = screen

        # 1. Carrega a imagem
        self.image = pygame.image.load('assets/sprites/trofeu.jpg').convert()

        # 2. Ajusta para o tamanho da tela
        self.image = pygame.transform.scale(self.image, (screen.get_width(), screen.get_height()))

    def draw(self):
        # Apenas desenha a imagem
        self.screen.blit(self.image, (0, 0))