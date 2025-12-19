# criando a tela inicial 
from .game import *
from src.settings import *

class TelaInicial:
        def __init__(self, screen):

            self.screen = screen

            self.fundo_inicial = pygame.image.load('assets\screens\Gemini_Generated_Image_f2oaynf2oaynf2oa.png').convert()
            self.fundo_inicial = pygame.transform.scale(self.fundo_inicial, (WINDOW_WIDTH, WINDOW_HEIGHT))  

        def draw(self):
            self.screen.blit(self.fundo_inicial, (0,0))
            pass

        