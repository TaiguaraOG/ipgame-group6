from .settings import *


class Obstaculos(pygame.sprite.Sprite):
    # Removi o 'dt' daqui, pois não precisamos dele na criação, só na atualização
    def __init__(self, pos, image, group):
        super().__init__(group)

        self.img_obs = pygame.image.load(image).convert_alpha()
        width = self.img_obs.get_width() * escala
        height = self.img_obs.get_height() * escala
        self.image = pygame.transform.scale(self.img_obs, (width, height))
        self.rect = self.image.get_rect(topleft=pos)

        self.velocidade_queda = 200

    def update(self, dt):
        # Aqui sim usamos o dt
        self.rect.y += self.velocidade_queda * dt

        # Destrói se sair da tela (economiza memória)
        if self.rect.top > MAP_HEIGHT:  # Melhor usar .top para garantir que saiu inteiro
            self.kill()