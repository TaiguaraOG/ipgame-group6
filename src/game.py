from .settings import *
from .player import Player
from .init_screen import TelaInicial
from .collectible_itens import Coletaveis

### começar a contruir a classe Game, a qual deve conter 
### __init__ (inicializando o basico do codigo), Run (com o loop principal), Events, Draw


class Game:
    def __init__(self):
        """
        """
        # 1 - def janela e superficie
        pygame.init()
        pygame.display.set_caption('CINtra')
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # valores presentes em settings
        self.game_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT)) # valores presentes em settings
        self.background = pygame.image.load('assets/sprites/background1.png')
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH,WINDOW_HEIGHT))


        # 2 - clock
        self.clock = pygame.time.Clock()
        self.running = True

        self.game_state = "MENU"  # (Ainda é necessário escrever a gerência dos estados em RUN)
        self.start_screen = TelaInicial(self.screen)

        # 3 - gerência dos grupos e spirts(FUTURO* -> Começado dia 15/12)
            ## Sprite -> É uma roupa 
            ## Rect -> O espaço delimitado (x,y) que vestirá a sprite
            ## Group -> evitar usar looping pra controlar os atores, actor.update() and actor.draw()

        self.all_sprites = pygame.sprite.Group()
        self.items = pygame.sprite.Group()


        # criando o objeto player
        
        self.player = Player(self.all_sprites)

        # criando os objetos coletaveis 

        self.item1 = Coletaveis("Lanche",(300,450), 'assets\sprites\coletavel1.png', self.items)
        self.item2 = Coletaveis("Arma",(440,450), 'assets\sprites\coletavel2.png', self.items)
        self.item3 = Coletaveis("Cracha",(600,450), 'assets\sprites\coletavel3.png', self.items)
    
        self.itens_coletados = {"Lanche" : 0, "Arma": 0, "Cracha": 0}

        # DEBBUGANDO

        print(f"tenho as seguintes sprites: {len(self.all_sprites)}") 
        print(f"player está na posição: {self.player.rect}")

        # FONTE DA HUD -> logica dentro de draw
        self.font = pygame.font.SysFont("Arial", 30, bold=True)

        




    def run(self):
        """
        Docstring for run
        
        :param self: Servindo para rodar o laço principal, atualizando os frames
        e checando os events (inclusive o QUIT)
        atualizando as ações e desenhando os eventos na tela atraves da intercomunicação com os metodos
        """
        while self.running:

            dt = self.clock.tick(FPS)/1000 # convertendo pra ms // valores presentes em settings

            self.events() # começar escrevendo so o quit, depois adicionar os demais 
            self.update(dt) 
            self.draw()

            pygame.display.flip()

    def events(self):

        
        for event in pygame.event.get():
            t = event.type
            if t == pygame.QUIT:
                self.running = False
                pygame.quit()
                quit()
        
            if self.game_state == 'MENU':
                if t == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.game_state = 'LIVE'
                        # debug 
                        print('o estado do jogo mudou pra LIVE')
            
            if self.game_state == 'LIVE':
                if t == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_state = 'MENU'
                        # debug
                        print('o jogador voltou para o MENU')

            

            ## terminar os demais eventos 
    
    def draw(self):
         # limpando a superficie 
        self.game_surface.blit(self.background, (0,0))

        if self.game_state == 'MENU':
            self.start_screen.draw() # objeto criado na linha 27

        if self.game_state == 'LIVE':
            # desenhando as sprites
            self.all_sprites.draw(self.game_surface)
            self.items.draw(self.game_surface)
            # criando a tela 
            self.screen.blit(self.game_surface,(0,0))

            # HUD RUDIMENTAR
            self.render_coletaveis = self.font.render( (
        f"Lanche: {self.itens_coletados['Lanche']}, "
        f"Arma: {self.itens_coletados['Arma']}, "
        f"Cracha: {self.itens_coletados['Cracha']}"
                                                     ), True, (0, 0, 0))
            # mostrando 
            self.screen.blit(self.render_coletaveis, (200,0))


    # pensar e estruturar isso daqui qnd tiver os obj
    def update(self, dt):
        # so atualizar se tiver na hora do jogo
        if self.game_state == 'LIVE':
            self.player.update(dt) # se comunicando com a logica de mov do jogador

            # colisao
            self.colisao = pygame.sprite.spritecollide(self.player, self.items, dokill=True)

            
            if self.colisao:
                for item in self.colisao:
                    print(f'coleteu: {item.name}')

                    if item.name == "Lanche":
                        self.itens_coletados["Lanche"] += 1
                    elif item.name == "Arma":
                        self.itens_coletados["Arma"] += 1
                    elif item.name == "Cracha":
                        self.itens_coletados["Cracha"] += 1
                

                    print(self.itens_coletados)

            
    
        