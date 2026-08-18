import sys

import pygame
from Nave import Nave
from Asteroid import Asteroid
from config.GameConfig import EngineConfig

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_titulo = pygame.font.SysFont("Arial", 48, bold=True)
        self.fonte_botao = pygame.font.SysFont("Arial", 28)

        self.largura_btn, self.altura_btn = 200,50
        self.btn_jogar = pygame.Rect(
            (EngineConfig.WIDTH // 2) - (self.largura_btn // 2),
            300,
            self.largura_btn,
            self.altura_btn,
        )

        # Cores
        self.COR_FUNDO = (15, 15, 25)
        self.COR_TEXTO = (255, 255, 255)
        self.COR_BOTAO = (0, 150, 200)
        self.COR_HOVER = (0, 200, 255)  # Cor quando o mouse passa por cima

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Botão esquerdo do mouse
                    # Se clicou no botão "Jogar", retorna True para iniciar o jogo
                    if self.btn_jogar.collidepoint(evento.pos):
                        return "JOGANDO"

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Enter também inicia
                    return "JOGANDO"

        return "MENU"

    def desenhar(self):
        self.tela.fill(self.COR_FUNDO)

        # 1. Desenhar o Título
        txt_titulo = self.fonte_titulo.render(
            "SPACE SHOOTER", True, self.COR_TEXTO
        )
        rect_titulo = txt_titulo.get_rect(
            center=(EngineConfig.WIDTH // 2, 180)
        )
        self.tela.blit(txt_titulo, rect_titulo)

        # 2. Desenhar o Botão com efeito de iluminação (Hover)
        pos_mouse = pygame.mouse.get_pos()
        cor_atual = (
            self.COR_HOVER
            if self.btn_jogar.collidepoint(pos_mouse)
            else self.COR_BOTAO
        )

        pygame.draw.rect(self.tela, cor_atual, self.btn_jogar, border_radius=10)

        # 3. Desenhar o Texto do Botão
        txt_jogar = self.fonte_botao.render("JOGAR", True, self.COR_TEXTO)
        rect_jogar = txt_jogar.get_rect(center=self.btn_jogar.center)
        self.tela.blit(txt_jogar, rect_jogar)

        pygame.display.flip()

class Jogo:
    def __init__(self):

        pygame.init()
        self.largura = EngineConfig.WIDTH
        self.altura = EngineConfig.HEIGHT
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Space Shooter - Projeto Base")

        self.estado = "MENU"
        self.menu = Menu(self.tela)

        self.clock = pygame.time.Clock()
        self.fps = EngineConfig.FPS
        self.dt = self.clock.tick(self.fps) / 1000.0
        self.pontos = 0

        # Elementos do jogo
        self.nave = Nave(self.largura, self.altura)
        self.asteroide = Asteroid(self.largura, self.altura)



    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.nave.processar_evento(evento)

    def checar_colisoes(self):
        # =========================================================================
        # TODO 4 (Alunos):
        # A) Tiro vs Asteroide:
        #    - Percorrer self.nave.tiros
        #    - Se tiro.colliderect(self.asteroide.rect):
        #        1. Remover o tiro da lista
        #        2. Reiniciar o asteroide (self.asteroide.iniciar_status())
        #        3. Incrementar self.pontos em 1
        #
        # B) Asteroide vs Nave:
        #    - Se self.nave.rect.colliderect(self.asteroide.rect):
        #        - Finalizar a partida (self.rodando = False ou reiniciar)
        # =========================================================================
        pass

    def atualizar(self):
        self.nave.atualizar()
        self.asteroide.mover()
        self.checar_colisoes()

    def desenhar(self):
        self.tela.fill((15, 15, 25))
        self.nave.desenhar(self.tela)
        self.asteroide.desenhar(self.tela)
        pygame.display.flip()

    def executar(self):
        while True:
            if self.estado == "MENU":
                # Processa eventos do menu e atualiza o estado se o botão for clicado
                self.estado = self.menu.processar_eventos()
                self.menu.desenhar()

            elif self.estado == "JOGANDO":
                self.processar_eventos()
                self.atualizar()
                self.desenhar()


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()