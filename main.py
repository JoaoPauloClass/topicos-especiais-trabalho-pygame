import sys

import pygame
from Nave import Nave
from Asteroid import Asteroid
from config import GameConfig
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
        self.fonte_info = pygame.font.SysFont("Arial", 14)
        self.largura_tela = tela.get_width()
        self.altura_tela = tela.get_height()


        # Cores
        self.COR_FUNDO = (15, 15, 25)
        self.COR_TEXTO = (255, 255, 255)
        self.COR_BOTAO_VOLTAR = (0, 150, 200)
        self.COR_BOTAO_CUSTOMIZAR = (150, 0, 200)
        self.COR_HOVER_JOGAR = (0, 200, 255)
        self.COR_HOVER_CUSTOMIZAR = (200, 0, 255)

        self.largura_btn, self.altura_btn = 200,50

        self.sprite_sheet = pygame.image.load(
            'sprites/fighters.png'
        ).convert_alpha()

        self.sprites = self.__get_sprites()

        self.opcoes_grid = self.__create_grid_opcoes()

        self.btn_voltar = pygame.Rect(
            self.altura_tela // 2 - 80, self.altura_tela - 70, 160 ,40
        )


    def __get_sprites(self):
        """
        Recorta o sprite sheet em 4 sprites diferentes
        """

        largura_total = self.sprite_sheet.get_width()
        altura_total = self.sprite_sheet.get_height()

        largura_s = largura_total // 2
        altura_s = altura_total // 2

        sprites = []

        for linha in range(2):
            for coluna in range(2):
                x = coluna * largura_s
                y = linha * altura_s

                rect_corte = pygame.Rect(x, y, largura_s, altura_s)

                sprite = self.sprite_sheet.subsurface(rect_corte)
                sprites.append(sprite)
        return sprites

    def __create_grid_opcoes(self):
        options = []
        square_size = 120
        gap = 30

        start_grid_x = (
            self.largura_tela - (2 * square_size + gap)
        ) // 2
        start_grid_y = 150

        for i in range(4):
            linha = i // 2
            coluna = i % 2

            x = start_grid_x + coluna * (square_size + gap)
            y = start_grid_y + linha * (square_size + gap)

            rect_quadro = pygame.Rect(x,y,square_size,square_size)
            options.append(rect_quadro)

        return options


    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                pos_mouse = pygame.mouse.get_pos()

                for index, rect_quadro in enumerate(self.opcoes_grid):
                    if rect_quadro.collidepoint(pos_mouse):
                        GameConfig.PlayerConfig.PLAYER_SHIP = index

                if self.btn_voltar.collidepoint(evento.pos):
                    return "MENU"

        return "CUSTOMIZANDO"

    def desenhar(self):
        self.tela.fill(self.COR_FUNDO)

        txt_titulo = self.fonte_titulo.render(
            "SELEÇÃO DE NAVE", True, self.COR_TEXTO
        )
        rect_titulo = txt_titulo.get_rect(
            center=(EngineConfig.WIDTH // 2, 50)
        )
        self.tela.blit(txt_titulo, rect_titulo)

        nave_atual = GameConfig.PlayerConfig.PLAYER_SHIP

        for index, rect_quadro in enumerate(self.opcoes_grid):
            if index == nave_atual:
                cor_borda = (0,255,255)
                largura_borda = 4
            else:
                cor_borda = (80,80,100)
                largura_borda = 2

            pygame.draw.rect(self.tela, (30,30,45), rect_quadro)
            pygame.draw.rect(
                self.tela, cor_borda, rect_quadro, width=largura_borda
            )

            sprite_nave = self.sprites[index]
            rect_quadro = sprite_nave.get_rect(center = rect_quadro.center)
            self.tela.blit(sprite_nave,rect_quadro)

            text_num = self.fonte_info.render(
                f"{index + 1}", True, (200,200,200)
            )

            self.tela.blit(text_num, (rect_quadro.x + 5, rect_quadro.y + 5))

        pygame.draw.rect(self.tela, self.COR_BOTAO_VOLTAR, self.btn_voltar,border_radius=5)

        txt_voltar = self.fonte_botao.render("VOLTAR", True, self.COR_TEXTO)
        rect_voltar = txt_voltar.get_rect(center=self.btn_voltar.center)


        self.tela.blit(txt_voltar, rect_voltar)

        pygame.display.flip()

class FimDeJogo:
    def __init__(self, tela):
        self.tela = tela
        self.largura = tela.get_width()
        self.altura = tela.get_height()

        self.fonte_titulo = pygame.font.SysFont("Arial", 48, bold=True)
        self.fonte_pontos = pygame.font.SysFont("Arial", 28, bold=True)
        self.fonte_botoes = pygame.font.SysFont("Arial", 22, bold=True)

        largura_btn = 200
        altura_btn = 50
        centro_x = self.largura // 2 - (largura_btn // 2)

        self.btn_reiniciar = pygame.Rect(centro_x, 320, largura_btn, altura_btn)

        # Botão Menu Principal
        self.btn_menu = pygame.Rect(
            centro_x, 390, largura_btn, altura_btn
        )

    def processar_eventos(self):
        """Lê cliques no mouse ou atalhos do teclado."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos_mouse = evento.pos

                if self.btn_reiniciar.collidepoint(pos_mouse):
                    return "JOGANDO"

                if self.btn_menu.collidepoint(pos_mouse):
                    return "MENU"

        return "FIMDEJOGO"

    def desenhar(self, pontos):
        self.tela.fill((20, 5, 5))

        texto_titulo = self.fonte_titulo.render(
            "VOCÊ PERDEU!", True, (255, 50, 50)
        )
        rect_titulo = texto_titulo.get_rect(
            center=(self.largura // 2, 140)
        )
        self.tela.blit(texto_titulo, rect_titulo)

        texto_pontos = self.fonte_pontos.render(
            f"Pontuação Final: {pontos}", True, (255, 255, 255)
        )
        rect_pontos = texto_pontos.get_rect(
            center=(self.largura // 2, 220)
        )
        self.tela.blit(texto_pontos, rect_pontos)

        # 3. DESENHO DOS BOTÕES
        pos_mouse = pygame.mouse.get_pos()

        # --- BOTÃO REINICIAR ---
        # Cor muda ao passar o mouse por cima (Hover)
        cor_btn_r = (
            (0, 180, 80)
            if self.btn_reiniciar.collidepoint(pos_mouse)
            else (0, 140, 60)
        )
        pygame.draw.rect(self.tela, cor_btn_r, self.btn_reiniciar, border_radius=8)

        txt_r = self.fonte_botoes.render(
            "JOGAR DE NOVO", True, (255, 255, 255)
        )
        self.tela.blit(
            txt_r, txt_r.get_rect(center=self.btn_reiniciar.center)
        )

        cor_btn_m = (
            (180, 50, 50)
            if self.btn_menu.collidepoint(pos_mouse)
            else (140, 40, 40)
        )
        pygame.draw.rect(self.tela, cor_btn_m, self.btn_menu, border_radius=8)

        txt_m = self.fonte_botoes.render(
            "MENU PRINCIPAL", True, (255, 255, 255)
        )
        self.tela.blit(txt_m, txt_m.get_rect(center=self.btn_menu.center))

        pygame.display.flip()

class Jogo:
    def __init__(self):

        pygame.init()
        self.largura = EngineConfig.WIDTH
        self.altura = EngineConfig.HEIGHT
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Space Shooter - Projeto Base")

        self.fonte_hud = pygame.font.SysFont("Arial", 20)

        self.clock = pygame.time.Clock()
        self.fps = GameConfig.EngineConfig.FPS
        self.pontos = 0

        self.estado = "MENU"
        self.menu = Menu(self.tela)
        self.customizacao = Customizar(self.tela)
        self.fimdejogo = FimDeJogo(self.tela)

        self.COR_BOTAO_VOLTAR = (0, 150, 200)
        self.btn_voltar = pygame.Rect(
            self.altura // 2 - 80, self.altura - 70, 160, 40
        )


        # Elementos do jogo
        self.nave = Nave(self.largura, self.altura, './sprites/fighters.png')

        self.asteroides = []

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if self.btn_voltar.collidepoint(evento.pos):
                    self.estado = "MENU"

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

        for tiro in self.nave.tiros[:]:
            for asteroide in self.asteroides:
                if tiro.colliderect(asteroide.rect):
                    self.nave.tiros.remove(tiro)

                    asteroide_destruido = asteroide.tomar_dano(
                        self.nave.dano_tiro
                    )
                    if asteroide_destruido:
                        asteroide.iniciar_status()
                        self.pontos += 10

                    break

        for asteroide in self.asteroides:
            if self.nave.rect.colliderect(asteroide.rect):

                self.nave.vida_atual -= 1

                asteroide.iniciar_status()

                if self.nave.vida_atual <= 0:
                    self.rodando = False
                break

        pass

    def atualizar_asteroides(self):
        while len(self.asteroides) <= 10:
            novo_asteroide = Asteroid(self.largura, self.altura, './sprites/asteroid.png')
            self.asteroides.append(novo_asteroide)

    def atualizar(self):
        self.nave.atualizar()

        for asteroide in self.asteroides:
            asteroide.mover()
        self.checar_colisoes()
        self.atualizar_asteroides()

        if self.nave.vida_atual <= 0:
            self.estado = "FIMDEJOGO"

    def desenhar(self):
        self.tela.fill((15, 15, 25))

        text_pontos = self.fonte_hud.render(f"Pontos: {self.pontos}", True, (255,255,255))
        self.tela.blit(text_pontos, (10, 10))

        cor_vida = (
        (0,255,120) if self.nave.vida_atual <= 0 else (255,60,60)
        )
        text_vida = self.fonte_hud.render(f"Vida: {self.nave.vida_atual}", True, (255,255,255))
        self.tela.blit(text_vida, (10, 40))

        self.nave.desenhar(self.tela)
        for asteroide in self.asteroides:
            asteroide.desenhar(self.tela)

        txt_voltar = self.fonte_hud.render("VOLTAR", True, (255,255,255))
        rect_voltar = txt_voltar.get_rect(center=self.btn_voltar.center)

        self.tela.blit(txt_voltar, rect_voltar)

        pygame.display.flip()

    def executar(self):
        while True:
            self.clock.tick(self.fps)
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

            elif self.estado == "FIMDEJOGO":
                self.estado = self.fimdejogo.processar_eventos()
                self.fimdejogo.desenhar(self.pontos)
                self.nave.resetar_vida()



if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()