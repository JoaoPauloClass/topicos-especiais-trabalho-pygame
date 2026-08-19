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

        self.largura_btn, self.altura_btn = 400,50
        self.btn_jogar = pygame.Rect(
            (EngineConfig.WIDTH // 2) - (self.largura_btn // 2),
            300,
            self.largura_btn,
            self.altura_btn,
        )
        self.btn_customizar_nave = pygame.Rect(
            (EngineConfig.WIDTH // 2) - (self.largura_btn // 2),
            400,
            self.largura_btn,
            self.altura_btn,
        )

        # Cores
        self.COR_FUNDO = (15, 15, 25)
        self.COR_TEXTO = (255, 255, 255)
        self.COR_BOTAO_JOGAR = (0, 150, 200)
        self.COR_BOTAO_CUSTOMIZAR = (150, 0, 200)
        self.COR_HOVER_JOGAR = (0, 200, 255) 
        self.COR_HOVER_CUSTOMIZAR = (200, 0, 255) 

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: 
                    if self.btn_jogar.collidepoint(evento.pos):
                        return "JOGANDO"
                    elif self.btn_customizar_nave.collidepoint(evento.pos):
                        return "CUSTOMIZANDO"

        return "MENU"

    def desenhar(self):
        self.tela.fill(self.COR_FUNDO)

        txt_titulo = self.fonte_titulo.render(
            "SPACE SHOOTER", True, self.COR_TEXTO
        )
        rect_titulo = txt_titulo.get_rect(
            center=(EngineConfig.WIDTH // 2, 180)
        )
        self.tela.blit(txt_titulo, rect_titulo)

        pos_mouse = pygame.mouse.get_pos()
        cor_atual_jogar = (
            self.COR_HOVER_JOGAR
            if self.btn_jogar.collidepoint(pos_mouse)
            else self.COR_BOTAO_JOGAR
        )
        
        cor_atual_customizar = (
            self.COR_HOVER_CUSTOMIZAR
            if self.btn_customizar_nave.collidepoint(pos_mouse)
            else self.COR_BOTAO_CUSTOMIZAR
        )

        pygame.draw.rect(self.tela, cor_atual_jogar, self.btn_jogar,border_radius=5)
        pygame.draw.rect(self.tela, cor_atual_customizar, self.btn_customizar_nave,border_radius=5)

        txt_jogar = self.fonte_botao.render("JOGAR", True, self.COR_TEXTO)
        rect_jogar = txt_jogar.get_rect(center=self.btn_jogar.center)
        
        txt_customizar = self.fonte_botao.render("CUSTOMIZAR NAVE", True, self.COR_TEXTO)
        rect_customizar = txt_customizar.get_rect(
            center=self.btn_customizar_nave.center
        )
        
        self.tela.blit(txt_jogar, rect_jogar)
        self.tela.blit(txt_customizar, rect_customizar)

        pygame.display.flip()

class Customizar:
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
        self.btn_customizar_nave = pygame.Rect(
            (EngineConfig.WIDTH // 2) - (self.largura_btn // 2),
            300,
            self.largura_btn,
            self.altura_btn,
        )

        # Cores
        self.COR_FUNDO = (15, 15, 25)
        self.COR_TEXTO = (255, 255, 255)
        self.COR_BOTAO_JOGAR = (0, 150, 200)
        self.COR_BOTAO_CUSTOMIZAR = (150, 0, 200)
        self.COR_HOVER_JOGAR = (0, 200, 255) 
        self.COR_HOVER_CUSTOMIZAR = (200, 0, 255) 

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: 
                    if self.btn_jogar.collidepoint(evento.pos):
                        return "JOGANDO"

        return "CUSTOMIZAR"

    def desenhar(self):
        self.tela.fill(self.COR_FUNDO)

        txt_titulo = self.fonte_titulo.render(
            "Customize sua nave", True, self.COR_TEXTO
        )
        rect_titulo = txt_titulo.get_rect(
            center=(EngineConfig.WIDTH // 2, 180)
        )
        self.tela.blit(txt_titulo, rect_titulo)

        pos_mouse = pygame.mouse.get_pos()
        cor_atual_jogar = (
            self.COR_HOVER_JOGAR
            if self.btn_jogar.collidepoint(pos_mouse)
            else self.COR_BOTAO_JOGAR
        )
        
        cor_atual_customizar = (
            self.COR_HOVER_CUSTOMIZAR
            if self.btn_customizar_nave.collidepoint(pos_mouse)
            else self.COR_BOTAO_CUSTOMIZAR
        )

        pygame.draw.rect(self.tela, cor_atual_jogar, self.btn_jogar,border_radius=5)
        pygame.draw.rect(self.tela, cor_atual_customizar, self.btn_customizar_nave,border_radius=5)

        txt_jogar = self.fonte_botao.render("JOGAR", True, self.COR_TEXTO)
        rect_jogar = txt_jogar.get_rect(center=self.btn_jogar.center)
        
        txt_customizar = self.fonte_botao.render("CUSTOMIZAR NAVE", True, self.COR_TEXTO)
        rect_customizar = txt_customizar.get_rect(
            center=(self.btn_jogar.centerx, self.btn_jogar.centery + 120)
        )
        
        self.tela.blit(txt_jogar, rect_jogar)
        self.tela.blit(txt_customizar, rect_customizar)

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
        self.customizacao = Customizar(self.tela)

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
                
            elif self.estado == "CUSTOMIZANDO":
                self.estado = self.customizacao.processar_eventos()
                self.customizacao.desenhar()


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()