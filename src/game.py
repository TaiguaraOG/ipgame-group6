from .settings import *
from .player import Player
from .init_screen import TelaInicial
from .collectible_itens import Coletaveis
from .obstaculos import Obstaculos
from .end_screen import VictoryScreen
from .game_over import GameOverScreen

### começar a contruir a classe Game, a qual deve conter 
### __init__ (inicializando o basico do codigo), Run (com o loop principal), Events, Draw


class Game:
    def __init__(self):


        # 1 - def janela e superficie

        pygame.init()
        pygame.display.set_caption('CINtra')
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # valores presentes em settings
        self.game_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT)) # valores presentes em settings
        self.background = pygame.image.load('assets/sprites/background1.png')
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH,WINDOW_HEIGHT))
        self.game_over_screen = GameOverScreen(self.screen)

        # 2 - clock

        self.clock = pygame.time.Clock()
        self.running = True

        self.game_state = "MENU"  # (Ainda é necessário escrever a gerência dos estados em RUN)
        self.start_screen = TelaInicial(self.screen)
        self.victory_screen = VictoryScreen(self.screen)

        # 3 - gerência dos grupos e spirts(FUTURO* -> Começado dia 15/12)
            ## Sprite -> É uma roupa 
            ## Rect -> O espaço delimitado (x,y) que vestirá a sprite
            ## Group -> evitar usar looping pra controlar os atores, actor.update() and actor.draw()

        self.all_sprites = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.g_obstaculo = pygame.sprite.Group()


        # criando o objeto player
        
        self.player = Player(self.all_sprites)

        # criando os objetos coletaveis 

        self.item1 = Coletaveis("Lanche",(300,450), 'assets/sprites/coletavel1.png', self.items)
        self.item2 = Coletaveis("Arma",(500,450), 'assets/sprites/coletavel2.png', self.items)
        self.item3 = Coletaveis("Cracha",(700,450), 'assets/sprites/coletavel3.png', self.items)
    
        self.itens_coletados = {"Lanche" : 0, "Arma": 0, "Cracha": 0}

        # DEBBUGANDO

        print(f"tenho as seguintes sprites: {len(self.all_sprites)}") 
        print(f"player está na posição: {self.player.rect}")

        # FONTE DA HUD -> logica dentro de draw
        self.font = pygame.font.SysFont("Arial", 30, bold=True)

        # criando o obstaculo 
       # self.obstaculo = Obstaculos((200,200, 'assets/sprites/obstaculo.jpg', self.g_obstaculo))
        
        # timer 
        self.timer_obstaculo = 0

    def reset_game(self):
        print("Reiniciando o jogo...")

        # 1. Reseta posição do Player
        self.player.rect.center = (100, 450)

        # 2. Limpa obstaculos antigos
        self.g_obstaculo.empty()

        # 3. Zera o contador de itens e recria o dicionário
        self.itens_coletados = {"Lanche": 0, "Arma": 0, "Cracha": 0}

        # 4. Recria os itens (pois eles foram deletados ao serem pegos)
        self.items.empty()

        # Recria os itens nas posições originais
        self.item1 = Coletaveis("Lanche", (300, 450), 'assets/sprites/coletavel1.png', self.items)
        self.item2 = Coletaveis("Arma", (500, 450), 'assets/sprites/coletavel2.png', self.items)
        self.item3 = Coletaveis("Cracha", (700, 450), 'assets/sprites/coletavel3.png', self.items)

        # 5. Voltar o estado para LIVE
        self.game_state = 'LIVE'

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
                        # Em vez de reescrever tudo, chamamos a função pronta:
                        self.reset_game()
                        print('NOVO JOGO INICIADO PELO MENU')

            if self.game_state == 'LIVE':
                if t == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_state = 'MENU'
                        print('o jogador voltou para o MENU')

            if self.game_state == 'VICTORY':
                if t == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.reset_game()  # Reseta o jogo e joga de novo
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False  # Sai do jogo

                        #  FIM DO JOGO AO ESBARRAR NO OBSTACULO
            if self.game_state == 'GAME_OVER':
                if t == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.reset_game()  # Tenta de novo!
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False  # Desiste

            ## terminar os demais eventos 

    def draw(self):
        # 1. SEGURANÇA: Pinta tudo de preto antes de desenhar qualquer coisa
        # Isso apaga a "sujeira" (barra verde) da tela de vitória anterior
        self.screen.fill((0, 0, 0))

        # 2. Desenha o background na superfície do jogo
        self.game_surface.blit(self.background, (0, 0))

        if self.game_state == 'MENU':
            self.start_screen.draw()

        if self.game_state == 'LIVE':
            self.all_sprites.draw(self.game_surface)
            self.items.draw(self.game_surface)
            self.g_obstaculo.draw(self.game_surface)

            # Passa a superfície do jogo para a tela principal
            self.screen.blit(self.game_surface, (0, 0))

            # HUD
            self.render_coletaveis = self.font.render(
                f"Lanche: {self.itens_coletados['Lanche']}, "
                f"Arma: {self.itens_coletados['Arma']}, "
                f"Cracha: {self.itens_coletados['Cracha']}",
                True, (0, 0, 0)
            )
            self.screen.blit(self.render_coletaveis, (200, 0))
            # vitoria ou derrota
        if self.game_state == 'VICTORY':
            self.victory_screen.draw()
        if self.game_state == 'GAME_OVER':
            self.game_over_screen.draw()

    # pensar e estruturar isso daqui qnd tiver os obj

    def update(self, dt):

        # so atualizar se tiver na hora do jogo
        if self.game_state == 'LIVE':

            self.player.update(dt) # se comunicando com a logica de mov do jogador
            self.g_obstaculo.update(dt) # tentando arrumar os coletaveis
            self.timer_obstaculo += dt

            if self.timer_obstaculo > 2:
                self.obstaculo = Obstaculos((random.randrange(200,800),0), 'assets/sprites/obstaculo.jpg', self.g_obstaculo)
                self.timer_obstaculo = 0 
                self.obstaculo.update(dt)


            # colisoes
            self.colisao_coletavel = pygame.sprite.spritecollide(self.player,self.items,dokill=True,collided=pygame.sprite.collide_rect_ratio(0.5))
            self.colisao_obstaculo = pygame.sprite.spritecollide(self.player,self.g_obstaculo,dokill=True,collided=pygame.sprite.collide_rect_ratio(0.6))

            

            if self.colisao_coletavel:
                for item in self.colisao_coletavel:
                    print(f'coletou: {item.name}')

                    if item.name == "Lanche":
                        self.itens_coletados["Lanche"] += 1
                    elif item.name == "Arma":
                        self.itens_coletados["Arma"] += 1
                    elif item.name == "Cracha":
                        self.itens_coletados["Cracha"] += 1
                

                    print(self.itens_coletados)

            if self.colisao_obstaculo:
                self.game_state = 'GAME_OVER'
                print('O jogador voltou para pro menu por conta de colisao')

                    # Verifica se pegou 1 de cada item
            tem_lanche = self.itens_coletados["Lanche"] >= 1
            tem_arma = self.itens_coletados["Arma"] >= 1
            tem_cracha = self.itens_coletados["Cracha"] >= 1

                    # Se tiver os 3 itens
            if tem_lanche and tem_arma and tem_cracha:
                self.game_state = 'VICTORY'  # Muda o estado
                print("JOGO FINALIZADO! PARABÉNS!")
    
