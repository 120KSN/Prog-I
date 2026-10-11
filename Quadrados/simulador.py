# importar o módulo pgzrun para rodar o jogo
import pgzrun
import random
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

quadr = [0] * 20
gravidade = 5

# primeiro bloco
for i in range(20):
    quadr[i] = Actor('quadrado.png')
    quadr[i].pos = (1800 / 19) * i, 10

# base
base = Actor('base.png')
base.pos = 900, 500

# largura e altura da janela
WIDTH = 1800
HEIGHT = 600

# desenhar na tela
def draw():
    screen.clear()
    for i in range(20):
        quadr[i].draw()
        base.draw()

# atualizar posições
def update():
    for i in range(20):
        if not quadr[i].colliderect(base):
            quadr[i].top += gravidade * ((i + 1) / 100)

# executar o jogo
pgzrun.go()

''' EXERCÍCIOS:

a) aumentar a velocidade de queda do quadrado
b) mudar a posição inicial do quadrado (colocar o quadrado mais alto)
c) mudar a posição da base (colocar a base mais para baixo)
d) mudar as figuras da base e do quadrado
e) colocar 2 quadrados caindo ao mesmo tempo

Para fazer as atividades a seguir, você deverá buscar na Internet/IA
como realizá-las no pygame zero:

f) alterar a cor de fundo da janela
===> "como alterar a cor de fundo da janela no pygame zero"
g) centralizar a janela na tela
===> "como centralizar a janela no pygame zero"
h) colocar um título na janela
===> "como colocar um título na janela no pygame zero"

'''
