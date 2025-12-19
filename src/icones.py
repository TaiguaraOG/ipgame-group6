from .settings import *

imagem_icone = pygame.image.load('assets\sprites\coletavel3.png')
escala_icones = 0.2
width_icones = int(imagem_icone.get_width() * escala_icones)
height_icone = int(imagem_icone.get_height() * escala_icones)