import pygame
from menus import Abertura, Menu, Configuracao, Credito
from selecao import SelecionarPersonagem, SelecionarFase

telaLargura = 1366
telaAltura = 768
estado = 0



try:
    pygame.init()
except:
    print("O modulo pygame não foi iniciado com sucesso")


tela = pygame.display.set_mode((telaLargura, telaAltura), pygame.FULLSCREEN, 32)
fps = pygame.time.Clock()

def init():
    global estado, tela
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = 9
        if estado == 0:
            estado = Abertura(tela, telaLargura, telaAltura)
        elif estado == 1:
            estado = Menu(tela, telaLargura, telaAltura)
        elif estado == 2:
            estado = Configuracao(tela)
        elif estado == 3:
            estado = Credito(tela)
        elif estado == 4:
            estado = SelecionarPersonagem(tela)
        elif estado == 5:
            estado = SelecionarFase(tela)
        elif estado == 6:
            estado = Luta(tela)
        elif estado == 7:
            estado = FimLuta(tela)
        elif estado == 8:
            estado = Pause(tela)
        elif estado == 9:
            Sair()

def Sair():
    pygame.quit()
    exit()



if __name__ == "__main__":
    init()