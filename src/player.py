from .settings import *
from .game_data import *


# criando uma classe player basica para representar na tela - Checkpoint II

class Player(pygame.sprite.Sprite):

    def __init__(self, group):

        super().__init__(group)

        self.image = pygame.image.load('assets/sprites/idle.png').convert_alpha()
        # analisando o tamanho para redimencionar
        width = (self.image.get_width() * escala)
        height = (self.image.get_height() * escala)
        self.speed = player_speed

        # redimencionando
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect(topleft = (0, 450))



    # recebendo as entradas 
    def input(self, dt):

        key = pygame.key.get_pressed() # retorna um dic !!!!!!!!!!!

        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.rect.x -= player_speed * dt
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.rect.x += player_speed * dt

    def update(self, dt):
        self.input(dt)

        # limitando por onde andar
        area_limite = pygame.Rect(0, 0, MAP_WIDTH, MAP_HEIGHT)
        self.rect.clamp_ip(area_limite)# https://www.pygame.org/docs/ref/rect.html#pygame.Rect.clamp_ip
        
        