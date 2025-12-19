# obstaculos 
"""
from .settings import *
# criar itens coletáveis
class Coletaveis(pygame.sprite.Sprite):

    def __init__(self, name, pos, imagem, group):

        super().__init__(group)
        self.name = name
        self.img = pygame.image.load(imagem).convert_alpha()
        width = (self.img.get_width() * escala)
        height = (self.img.get_height() * escala)

        self.image = pygame.transform.scale(self.img, (width,height))
        self.rect = self.image.get_rect(topleft = pos)
"""


from .settings import *

class Obstaculos(pygame.sprite.Sprite):

    def __init__(self,pos, image, group, dt):
        super().__init__(group)

        self.img_obs = pygame.image.load(image).convert_alpha()
        width = self.img_obs.get_width() * escala_obstaculo
        height =  self.img_obs.get_height() * escala_obstaculo
        self.image = pygame.transform.scale(self.img_obs, (width, height))
        self.rect = self.image.get_rect(topleft = pos)
        pygame.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), 2)
        self.velocidade_queda = 200
        
    def update(self, dt):

        self.rect.y += self.velocidade_queda * dt
        if self.rect.y > MAP_HEIGHT:
            self.kill()


    

