import pygame

class Personagem(object):

    back = [False]
    blockDown = [False]
    blockIdle = [False]
    down = [False]
    fall = [False]
    hitDown = [False]
    hitIdle = [False]
    idle = [False]
    jump = [False]
    kickDown = [False]
    kickIdle = [False]
    punchDown = [False]
    punchIdle = [False]
    strongKickDown = [False]
    strongKickIdle = [False]
    strongPunchDown = [False]
    strongPunchIdle = [False]
    walk = [False]

    velocidade = 20
    frente = False
    tras =  False
    Pula = False
    image = 0

    x = 0
    y = 0
    i = 1

    def loadMove(self, nome, nomeMove):
        move = []
        for i in range(1, 10):
            try:
                move.append(pygame.image.load(f"GameFiles/Imagens/Sprites/move.{nome}/{nomeMove}/{i}.png"))
            except:
                break
        return move

    def __init__(self, nome):
        self.back = self.loadMove(nome, "back")
        self.blockDown = self.loadMove(nome, "blockDown")
        self.blockIdle = self.loadMove(nome, "blockIdle")
        self.down = self.loadMove(nome, "down")
        self.fall = self.loadMove(nome, "fall")
        self.hitDown = self.loadMove(nome, "hitDown")
        self.hitIdle = self.loadMove(nome, "hitIdle")
        self.idle = self.loadMove(nome, "idle")
        self.jump = self.loadMove(nome, "jump")
        self.kickDown = self.loadMove(nome, "kickDown")
        self.kickIdle = self.loadMove(nome, "kickIdle")
        self.punchDown = self.loadMove(nome, "punchDown")
        self.punchIdle = self.loadMove(nome, "punchIdle")
        self.strongKickDown = self.loadMove(nome, "strongKickDown")
        self.strongKickIdle = self.loadMove(nome, "strongKickIdle")
        self.strongPunchDown = self.loadMove(nome, "strongPunchDown")
        self.strongPunchIdle = self.loadMove(nome, "strongPuchIdle")
        self.walk = self.loadMove(nome, "walk")


    def GetRect(self, image):
        return pygame.Rect((self.x, self.y), image.get_size())

    def Back(self):
        if self.back[0]:
            self.back[0] = False
        else:
            self.back[0] = True

    def BlockDown(self):
        if self.blockDown[0]:
            self.blockDown[0] = False
        else:
            self.blockDown[0] = True

    def BlockIdle(self):
        if self.blockIdle[0]:
            self.blockIdle[0] = False
        else:
            self.blockIdle[0] = True

    def Down(self):
        if self.down[0]:
            self.down[0] = False
        else:
            self.down[0] = True

    def Fall(self):
        if self.fall[0]:
            self.fall[0] = False
        else:
            self.fall[0] = True

    def HitDown(self):
        if self.hitDown[0]:
            self.hitDown[0] = False
        else:
            self.hitDown[0] = True

    def HitIdle(self):
        if self.hitIdle[0]:
            self.hitIdle[0] = False
        else:
            self.hitIdle[0] = True

    def Idle(self):
        if self.idle[0]:
            self.idle[0] = False
        else:
            self.idle[0] = True

    def Jump(self):
        if self.jump[0]:
            self.jump[0] = False
        else:
            self.jump[0] = True

    def KickDown(self):
        if self.kickDown[0]:
            self.kickDown[0] = False
        else:
            self.kickDown[0] = True

    def KickIdle(self):
        if self.kickIdle]:
            self.kickIdle[0] = False
        else:
            self.kickIdle[0] = True

    def PunchDown(self):
        if self.punchDown[0]:
            self.punchDown[0] = False
        else:
            self.punchDown[0] = True

    def PunchIdle(self):
        if self.punchIdle[0]:
            self.punchIdle[0] = False
        else:
            self.punchIdle[0] = True

    def StrongKickDown(self):
        if self.strongKickDown[0]:
            self.strongKickDown[0] = False
        else:
            self.strongKickDown[0] = True

    def StrongKickIdle(self):
        if self.strongKickIdle[0]:
            self.strongKickIdle[0] = False
        else:
            self.strongKickIdle[0] = True

    def StrongPunchDown(self):
        if self.strongPunchDown[0]:
            self.strongPunchDown[0] = False
        else:
            self.strongPunchDown[0] = True

    def StrongPunchIdle(self):
        if self.StrongPunchIdle()[0]:
            self.StrongPunchIdle()[0] = False
        else:
            self.StrongPunchIdle()[0] = True

    def Walk(self):
        if self.walk[0]:
            self.walk[0] = False
        else:
            self.walk[0] = True

    def update(self):
        if self.walk:
            self.x += self.velocidade
            try:
                self.image = self.walk[self.i]
                self.i += 1
            except:
                self.image = self.walk[1]
                self.i = 1

        if self.back:
            self.x -= self.velocidade
            try:
                self.image = self.back[self.i]
                self.i -= 1
            except:
                self.image = self.back[len(self.walk)-1]
                self.i = len(self.back)-1

        if self.down[0]:
            self.i = 1
            try:
                self.image = self.down[0]
                self.i += 1
            except:
                self.i -=1

        if not self.back[0] and not self.walk[0] and not down[0]:
            try:
                self.image = self.idle[self.i]
                self.i += 1
            except:
                self.image = self.idle[1]
                self.i = 1

