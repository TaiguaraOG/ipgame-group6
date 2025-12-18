from .settings import *
from .player import Player
from .init_screen import TelaInicial
from .collectible_itens import Coletaveis
from .obstaculos import Obstaculos
from .icones import *


### começar a contruir a classe Game, a qual deve conter 
### __init__ (inicializando o basico do codigo), Run (com o loop principal), Events, Draw


class Game:
    def __init__(self):


        # 1 - def janela e superficie

        pygame.init()
        pygame.display.set_caption('CINtra')
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # valores presentes em settings
        self.game_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT)) # valores presentes em settings
        self.background = pygame.image.load('C:/projeto_ip/ipgame-group6/assets/sprites/background1.png')
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
        self.g_obstaculo = pygame.sprite.Group()


        # icones
        self.imagem_icone_item_1 = pygame.image.load('C:/projeto_ip/ipgame-group6/assets/sprites/coletavel1.png')
        self.imagem_icone_item_1 = pygame.transform.scale(self.imagem_icone_item_1, (width_icones, height_icone))
        self.imagem_icone_item_2 = pygame.image.load('C:/projeto_ip/ipgame-group6/assets/sprites/coletavel2.png')
        self.imagem_icone_item_2 = pygame.transform.scale(self.imagem_icone_item_2, (width_icones, height_icone))
        self.imagem_icone_item_3 = pygame.image.load('C:/projeto_ip/ipgame-group6/assets/sprites/coletavel3.png')
        self.imagem_icone_item_3 = pygame.transform.scale(self.imagem_icone_item_3, (width_icones, height_icone))


        # criando o objeto player
        
        self.player = Player(self.all_sprites)

        # criando os objetos coletaveis 

        self.item1 = Coletaveis("Lanche",(300,450), 'C:/projeto_ip/ipgame-group6/assets/sprites/coletavel1.png', self.items)
        self.item2 = Coletaveis("Arma",(440,450), 'C:/projeto_ip/ipgame-group6/assets/sprites/coletavel2.png', self.items)
        self.item3 = Coletaveis("Cracha",(600,450), 'C:/projeto_ip/ipgame-group6/assets/sprites/coletavel3.png', self.items)
    
        self.itens_coletados = {"Lanche" : 0, "Arma": 0, "Cracha": 0}

        # DEBBUGANDO

        print(f"tenho as seguintes sprites: {len(self.all_sprites)}") 
        print(f"player está na posição: {self.player.rect}")

        # FONTE DA HUD -> logica dentro de draw
        self.font = pygame.font.SysFont("Arial", 30, bold=True)

        # criando o obstaculo 
       # self.obstaculo = Obstaculos((200,200, 'assets\sprites\obstaculo.jpg', self.g_obstaculo))
        
        # timer 
        self.timer_obstaculo = 0




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
            self.g_obstaculo.draw(self.game_surface)
            # criando a tela 
            self.screen.blit(self.game_surface,(0,0))

            # tentando ver a hitbox

            pygame.draw.rect(self.game_surface, (250, 0, 0), self.player.hitbox, 2)

            # mostra os itens e a quantidade 
            self.screen.blit(self.imagem_icone_item_1, (10, 10))
            self.screen.blit(self.imagem_icone_item_2, (10, 60))
            self.screen.blit(self.imagem_icone_item_3, (10, 110))

            self.render_item_1 = self.font.render((f"x {self.itens_coletados['Lanche']}"), True, (0, 0, 0))
            self.render_item_2 = self.font.render((f"x {self.itens_coletados['Arma']}"), True, (0, 0, 0))
            self.render_item_3 = self.font.render((f"x {self.itens_coletados['Cracha']}"), True, (0, 0, 0))

            # mostrando 
            self.screen.blit(self.render_item_1, (60,10))
            self.screen.blit(self.render_item_2, (60,60))
            self.screen.blit(self.render_item_3, (60,110))


    # pensar e estruturar isso daqui qnd tiver os obj

    def update(self, dt):

        # so atualizar se tiver na hora do jogo
        if self.game_state == 'LIVE':

            self.player.update(dt) # se comunicando com a logica de mov do jogador
            self.g_obstaculo.update(dt) # tentando arrumar os coletaveis
            self.timer_obstaculo += dt

            if self.timer_obstaculo > 2:
                self.obstaculo = Obstaculos((random.randrange(200,800),0), 'C:/projeto_ip/ipgame-group6/assets/sprites/obstaculo.jpg', self.g_obstaculo, dt)
                self.timer_obstaculo = 0 
                self.obstaculo.update(dt)


            # colisoes -- V1.2 as colisões sao baseadas na hitboxe agora, e n no rect da imagem

            self.colisao_coletavel = pygame.sprite.spritecollide(self.player, self.items, dokill=True)

            self.colisao_obstaculo = False

            for obstaculo in self.g_obstaculo:
                if self.player.hitbox.colliderect(obstaculo.rect):
                    self.colisao_obstaculo = True
                    obstaculo.kill()
                    break
            

            if self.colisao_coletavel:
                for item in self.colisao_coletavel:
                    print(f'coleteu: {item.name}')

                    if item.name == "Lanche":
                        self.itens_coletados["Lanche"] += 1
                    elif item.name == "Arma":
                        self.itens_coletados["Arma"] += 1
                    elif item.name == "Cracha":
                        self.itens_coletados["Cracha"] += 1
                

                    print(self.itens_coletados)

            if self.colisao_obstaculo:
                    # mudar isso depois 
                self.game_state = 'MENU'
                print('O jogador voltou para pro menu por conta de colisao')

            
    
        