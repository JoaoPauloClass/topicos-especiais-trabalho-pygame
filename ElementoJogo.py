import pygame

class ElementoJogo(pygame.sprite.Sprite):
    """Classe base para todos os objetos do jogo."""
    def __init__(self, x, y, largura, altura, caminho_sprite, velocidade=5):
        super().__init__()
        self.velocidade = velocidade

        self.image = pygame.image.load(caminho_sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (largura, altura))

        self.rect = self.image.get_rect()
    def mover(self):
        """Método de movimentação a ser sobrescrito ou estendido pelas subclasses."""
        pass

    def desenhar(self, tela):
        """Desenho padrão (retângulo) caso a subclasse não sobrescreva."""
        tela.blit(self.image, (self.rect.x, self.rect.y))