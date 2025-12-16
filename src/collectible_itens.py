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