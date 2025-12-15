from .settings import *

# criando uma classe player basica para representar na tela - Checkpoint II

class Player(pygame.sprite.Sprite):

    def __init__(self, group):

        super().__init__(group)
        self.image = pygame.image.load(r'C:\Users\maseo\ipgame-group6\assets\sprites\idle.png').convert_alpha()
        # analisando o tamanho para redimencionar
        width = (self.image.get_width() * escala)
        height = (self.image.get_height() * escala)
        # redimencionando
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect(topleft = (0, 200))

        # lembrar do video q vi sobre self.hitbox_rect


    def update(self, dt):
        pass