from .settings import *
# criar itens coletáveis

# função solitaria, n faz parte da classe 

def posicao_item():

    posicoes = [(100, 450)] # tupla!!!!! a p1 é a do player
    margem = 50
    distancia_min = 30 # poderia ter uma logica melhor no lugar aqui, assim tem overlap as vezes 

    while len(posicoes) < 4:

        x = random.randrange(margem, MAP_WIDTH - margem) # respeitando o eixo x e sua margem
        y = 450 # (essa altura_fixa no game_data dps)


        posicao_ok = True

        for pos in posicoes:
            # abs pra calcular os dois lados

            if abs(x - pos[0]) < distancia_min: 
                posicao_ok = False

        if posicao_ok:
            posicoes.append((x,y))

    return posicoes[1:]



class Coletaveis(pygame.sprite.Sprite):

    def __init__(self, name, pos, imagem, group):

        super().__init__(group)
        self.name = name
        self.img = pygame.image.load(imagem).convert_alpha()
        width = (self.img.get_width() * escala)
        height = (self.img.get_height() * escala)

        self.image = pygame.transform.scale(self.img, (width,height))
        self.rect = self.image.get_rect(topleft = pos)

    def posiçao_item(self):

        self.n_itens = []
        margem = 50  # mudar pro gamedata dps




