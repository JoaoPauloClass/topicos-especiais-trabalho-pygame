import pygame
from ElementoJogo import ElementoJogo
from config import GameConfig
from config.GameConfig import PlayerConfig

class Nave(ElementoJogo):
    def __init__(self, largura_tela, altura_tela,caminho_sprite, velocidade=6, ):
        # Inicializa a classe base com posição inicial centralizada embaixo
        super().__init__(
            x=largura_tela // 2 - 20,
            y=altura_tela - 60,
            largura=40,
            altura=40,
            velocidade=PlayerConfig.PLAYER_VELOCITY,
            caminho_sprite='./sprites/fighters.png'
        )
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.vel_x = 0
        self.tiros = []  # Lista que guardará os tiros ativos

        self.sprite_sheet = pygame.image.load(caminho_sprite)
        self.player_ship = self.__get_ship_sprite(GameConfig.PlayerConfig.PLAYER_SHIP)
        self.rect = self.player_ship.get_rect()

        self.rect.centerx = largura_tela // 2
        self.rect.bottom = altura_tela

    def processar_evento(self, evento):
        """Controla os eventos de teclado para movimentação e disparo."""
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                self.vel_x = -self.velocidade
            elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                self.vel_x = self.velocidade
            elif evento.key == pygame.K_SPACE:
                self.atirar()

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
        # =========================================================================
        # TODO 1 (Alunos): Criar um projétil (pygame.Rect) saindo da ponta da nave
        # (ex: largura 4, altura 10) e adicioná-lo à lista self.tiros
        # =========================================================================
        pass

    def atualizar_tiros(self):
        # =========================================================================
        # TODO 2 (Alunos):
        # - Mover cada tiro da lista para cima (diminuir tiro.y)
        # - Remover da lista os tiros que saírem pelo topo da tela (tiro.bottom < 0)
        # =========================================================================
        pass

    def atualizar(self):
        self.mover()
        self.atualizar_tiros()

    def desenhar(self, tela):
        # Polimorfismo: renderiza a nave e acordo com oq o player pegou
        tela.blit(self.player_ship, self.rect)

        # Desenha os tiros ativos na cor branca
        for tiro in self.tiros:
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
