import pygame


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen

        # 1. Carrega a imagem de Game Over
        try:
            self.image = pygame.image.load('assets/sprites/gameover.png').convert()
            # 2. Estica para o tamanho da tela
            self.image = pygame.transform.scale(self.image, (screen.get_width(), screen.get_height()))
        except FileNotFoundError:
            print("ERRO: Imagem 'gameover.png' não encontrada!")
            self.image = None

    def draw(self):
        if self.image:
            self.screen.blit(self.image, (0, 0))
        else:
            # Se não tiver imagem, pinta de vermelho pra avisar
            self.screen.fill((255, 0, 0))