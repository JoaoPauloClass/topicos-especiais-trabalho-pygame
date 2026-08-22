import pygame
from ElementoJogo import ElementoJogo
from config import GameConfig
from config.GameConfig import PlayerConfig

class Nave(ElementoJogo):
    def __init__(self, largura_tela, altura_tela,caminho_sprite, velocidade=6, ):

        self.id_nave = GameConfig.PlayerConfig.PLAYER_SHIP

        dados_nave = GameConfig.ShipConfig.DADOS_NAVES.get(
            self.id_nave, GameConfig.ShipConfig.DADOS_NAVES[0]
        )

        self.nome = dados_nave["nome"]
        self.vida_maxima = dados_nave["vida"]
        self.vida_atual = dados_nave["vida"]
        self.dano_tiro = dados_nave["dano_tiro"]
        self.vel_tiro = dados_nave["vel_tiro"]
        self.cooldown_tiro = dados_nave[
            "cooldown"
        ]
        # Inicializa a classe base com posição inicial centralizada embaixo
        super().__init__(
            x=largura_tela // 2 - 20,
            y=altura_tela - 60,
            largura=40,
            altura=40,
            velocidade=dados_nave["velocidade"],
            caminho_sprite='./sprites/fighters.png'
        )
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.vel_x = 0
        self.tiros = []  # Lista que guardará os tiros ativos
        self.ultimo_disparo = pygame.time.get_ticks()

        self.sprite_sheet = pygame.image.load(caminho_sprite)
        self.player_ship = self.__get_ship_sprite(GameConfig.PlayerConfig.PLAYER_SHIP)
        self.rect = self.player_ship.get_rect()

        self.rect.centerx = largura_tela // 2
        self.rect.bottom = altura_tela


    def resetar_vida(self):
        self.vida_atual = self.vida_maxima

    def processar_evento(self, evento):
        """Controla os eventos de teclado para movimentação e disparo."""
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                self.vel_x = -self.velocidade
            elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                self.vel_x = self.velocidade

        elif evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_a) and self.vel_x < 0:
                self.vel_x = 0
            elif evento.key in (pygame.K_RIGHT, pygame.K_d) and self.vel_x > 0:
                self.vel_x = 0

    def mover(self):
        """Aplica o deslocamento horizontal e trava nas bordas da tela."""
        self.rect.x += self.vel_x

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > (self.largura_tela - 120):
            self.rect.right = (self.largura_tela - 120)

    def atirar(self):
        if PlayerConfig.PLAYER_SHIP == 2:
            largura_tiro = 8
            altura_tiro = 100
        else:
            largura_tiro = 6
            altura_tiro = 25

        agora = pygame.time.get_ticks()
        intervalo_ms_tiro = max(50, int(self.cooldown_tiro * 1000))

        if agora - self.ultimo_disparo >= intervalo_ms_tiro:
            self.ultimo_disparo = agora

            # Posiciona o tiro no centro horizontal da nave (rect.centerx) e na ponta superior (rect.top)
            tiro_x = self.rect.centerx - (largura_tiro // 2)
            tiro_y = self.rect.top - altura_tiro + 60

            novo_tiro = pygame.Rect(tiro_x, tiro_y, largura_tiro, altura_tiro)
            self.tiros.append(novo_tiro)


    def atualizar_tiros(self):
        # Itera sobre uma cópia da lista self.tiros[:] para poder remover sem dar erro no loop
        for tiro in self.tiros[:]:
            tiro.y -= self.vel_tiro

            if tiro.bottom < 0:
                self.tiros.remove(tiro)

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            self.atirar()

        self.mover()
        self.atualizar_tiros()
        self.player_ship = self.__get_ship_sprite(GameConfig.PlayerConfig.PLAYER_SHIP)

    def desenhar(self, tela):
        # Polimorfismo: renderiza a nave e acordo com oq o player pegou
        tela.blit(self.player_ship, self.rect)

        # Desenha os tiros ativos na cor branca
        for tiro in self.tiros:
            if GameConfig.PlayerConfig.PLAYER_SHIP == 2:
                pygame.draw.rect(tela, (200, 0, 0), tiro)
            else:
                pygame.draw.rect(tela, (255, 255, 255), tiro)

    def __get_ship_sprite(self, player_ship=1):
        #méto-do privado da classe para separa o sprite sheet e passar um sprite unico para o metodo de desenho
        largura_total_sprite_sheet = self.sprite_sheet.get_width()
        altura_total_sprite_sheet = self.sprite_sheet.get_height()

        largura_sprite = largura_total_sprite_sheet // 2
        altura_sprite = altura_total_sprite_sheet // 2

        sprites = []
        for linha in range(2):
            for coluna in range(2):
                x = linha * largura_sprite
                y = coluna * altura_sprite

                rect_corte = pygame.Rect(x, y, largura_sprite, altura_sprite)
                sprites.append(self.sprite_sheet.subsurface(rect_corte))

        return sprites[player_ship]
