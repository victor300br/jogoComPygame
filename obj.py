import pygame
class Obj(pygame.sprite.Sprite):
    def __init__(self,imagem,x,y,*grupo):
        super().__init__(*grupo)
        self.image=pygame.image.load(imagem)
        self.rect=self.image.get_rect()
        self.rect[0]=x
        self.rect[1]=y
    def colisao(self,x_maca):
        self.image=pygame.image.load('jogo_da_inf/cobrinha/fundo.png')
        #x_maca+600
        # self.kill()   
