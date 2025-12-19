from .settings import *
from .player import Player
from .init_screen import TelaInicial
from .collectible_itens import Coletaveis, posicao_item
from .obstaculos import Obstaculos
from .end_screen import VictoryScreen
from .game_over import GameOverScreen
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


        # icones
        self.imagem_icone_item_1 = pygame.image.load('assets\sprites\coletavel1.png')
        self.imagem_icone_item_1 = pygame.transform.scale(self.imagem_icone_item_1, (width_icones, height_icone))
        self.imagem_icone_item_2 = pygame.image.load('assets\sprites\coletavel2.png')
        self.imagem_icone_item_2 = pygame.transform.scale(self.imagem_icone_item_2, (width_icones, height_icone))
        self.imagem_icone_item_3 = pygame.image.load('assets/sprites/coletavel3.png')
        self.imagem_icone_item_3 = pygame.transform.scale(self.imagem_icone_item_3, (width_icones, height_icone))


        # criando o objeto player
        
        self.player = Player(self.all_sprites)

        # criando os objetos coletaveis 

        posicoes = posicao_item()
        self.item1 = Coletaveis("Lanche", posicoes[0], 'assets\sprites\coletavel1.png', self.items)
        self.item2 = Coletaveis("Arma", posicoes[1], 'assets\sprites\coletavel2.png', self.items)
        self.item3 = Coletaveis("Cracha", posicoes[2], 'assets\sprites\coletavel3.png', self.items)

        self.itens_coletados = {"Lanche" : 0, "Arma": 0, "Cracha": 0}
        self.pontuação = 0 
        self.pontuação_vitoria = 10
        self.valor_itens = {"Lanche": 2, "Arma": 3, "Cracha": 5}
        

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
        self.pontuação = 0

        # 4. Recria os itens (pois eles foram deletados ao serem pegos)
        self.items.empty()

        # Recria os itens nas posições originais # Mod por Taiguara -> posicao aleataria dos intens 
        posicoes = posicao_item()
        self.item1 = Coletaveis("Lanche", posicoes[0], 'assets/sprites/coletavel1.png', self.items)
        self.item2 = Coletaveis("Arma", posicoes[1], 'assets/sprites/coletavel2.png', self.items)
        self.item3 = Coletaveis("Cracha", posicoes[2], 'assets/sprites/coletavel3.png', self.items)

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

            # test pra ver os ponto
            self.render_pontuação = self.font.render(f"pontuação: {self.pontuação}/ {self.pontuação_vitoria}", True, (0, 0, 0))
            self.screen.blit(self.render_pontuação, (10, 160))

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
                    print(f'coletou: {item.name}')

                    if item.name == "Lanche":
                        self.itens_coletados["Lanche"] += 1
                        self.pontuação += self.valor_itens["Lanche"]
                    elif item.name == "Arma":
                        self.itens_coletados["Arma"] += 1
                        self.pontuação += self.valor_itens["Arma"]
                    elif item.name == "Cracha":
                        self.itens_coletados["Cracha"] += 1
                        self.pontuação += self.valor_itens["Cracha"]
                

                    print(self.itens_coletados)

            if self.colisao_obstaculo:
                self.game_state = 'GAME_OVER'
                print('O jogador voltou para pro menu por conta de colisao')

                    # Verifica se pegou 1 de cada item
            tem_lanche = self.itens_coletados["Lanche"] >= 1
            tem_arma = self.itens_coletados["Arma"] >= 1
            tem_cracha = self.itens_coletados["Cracha"] >= 1

                    # se atingir a pontuação
            if self.pontuação >= self.pontuação_vitoria:
                self.game_state = 'VICTORY'  # Muda o estado
                print("JOGO FINALIZADO! PARABÉNS!")
    
