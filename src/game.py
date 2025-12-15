from .settings import *

### começar a contruir a classe Game, a qual deve conter 
### __init__ (inicializando o basico do codigo), Run (com o loop principal), Events, Draw


class Game:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        # 1 - def janela e superficie
        pygame.init()
        pygame.display.set_caption('CINtra')
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # valores presentes em settings
        self.game_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT)) # valores presentes em settings
        
        # 2 - clock
        self.clock = pygame.time.Clock()
        self.running = True

        # self.game_state = "start_game" (Ainda é necessário escrever a gerência dos estados em RUN)

        # 3 - gerência dos grupos (FUTURO)



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


            ## terminar os demais eventos 
    
    def draw(self):

        # limpando a superficie 
        self.game_surface.fill(background_color)

        # desenha a supercifie
        self.screen.blit(self.game_surface,(0,0))

    # pensar e estruturar isso daqui qnd tiver os obj
    def update(self, dt):
        pass
