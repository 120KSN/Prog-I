# importar o módulo pgzrun para rodar o jogo
import os
import pgzrun
import random
import pygame
import sys

# Força a centralização da janela do Pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'

contador = 0
quantidade_quadrados = 50
quadr = [0] * quantidade_quadrados
minimo = -5
maximo = 5
cor_minima = 20
cor_maxima = 255
velocidade = 5
velocidade_y = [5] * quantidade_quadrados
velocidade_x = [5] * quantidade_quadrados

# CLAUDE
pares_em_cooldown = {}
COOLDOWN_FRAMES = 10

for i in range(quantidade_quadrados):
    quadr[i] = Actor('quadrado.png')
    quadr[i].pos = random.randint(0, 1536 - 50), random.randint(0, 864 - 50)
    quadr[i].cor_atual = (cor_maxima, cor_maxima, cor_maxima)            # Guarda a cor na memória
    quadr[i].imagem_limpa = pygame.image.load("images/quadrado.png").convert_alpha()

# definir largura e altura da janela
WIDTH = 1920
HEIGHT = 1080

# método que vai desenhar os atores na tela
def draw():
    # limpar a tela
    screen.clear()
    screen.fill("gray")
    for i in range(quantidade_quadrados):
        quadr[i]._surf = quadr[i].imagem_limpa.copy()
        quadr[i]._surf.fill(quadr[i].cor_atual, special_flags=pygame.BLEND_RGBA_MULT)
        quadr[i].draw() # Desenha na tela

# método que vai atualizar a posição dos atores
def update():
    global velocidade_x, velocidade_y, contador, pares_em_cooldown, quantidade_quadrados
    quantidade_quadrados = len(quadr)

    # Decrementa cooldowns
    pares_em_cooldown = {par: v - 1 for par, v in pares_em_cooldown.items() if v > 1}

    for i, quad in enumerate(quadr):
        quad.y += velocidade_y[i]
        quad.x += velocidade_x[i]

        # Colisão com bordas
        if quad.left < 0:
            quad.left = 0
            velocidade_x[i] = abs(velocidade_x[i])
            velocidade_y[i] = random.randint(minimo, maximo)
        elif quad.right > WIDTH:
            quad.right = WIDTH
            velocidade_x[i] = -abs(velocidade_x[i])
            velocidade_y[i] = random.randint(minimo, maximo)

        if quad.top < 0:
            quad.top = 0
            velocidade_y[i] = abs(velocidade_y[i])
            velocidade_x[i] = random.randint(minimo, maximo)
        elif quad.bottom > HEIGHT:
            quad.bottom = HEIGHT
            velocidade_y[i] = -abs(velocidade_y[i])
            velocidade_x[i] = random.randint(minimo, maximo)

        # Colisão entre quadrados
        for j, q in enumerate(quadr):
            if j <= i:
                continue  # evita checar o mesmo par duas vezes

            par = (i, j)
            if par in pares_em_cooldown:
                continue  # ainda em cooldown, ignora

            if quad.colliderect(q):
                # --- Separação física ---
                dx = q.x - quad.x
                dy = q.y - quad.y
                dist = max((dx**2 + dy**2) ** 0.5, 1)

                # Empurra cada um para fora metade da sobreposição
                sobreposicao = 50  # tamanho aproximado do quadrado
                empurra = (sobreposicao - dist) / 2 + 1
                quad.x -= int(dx / dist * empurra)
                quad.y -= int(dy / dist * empurra)
                q.x    += int(dx / dist * empurra)
                q.y    += int(dy / dist * empurra)

                # --- Troca de velocidades (conservação de momento simples) ---
                velocidade_x[i], velocidade_x[j] = velocidade_x[j], velocidade_x[i]
                velocidade_y[i], velocidade_y[j] = velocidade_y[j], velocidade_y[i]

                # --- Cores aleatórias ---
                quad.cor_atual = (random.randint(cor_minima, cor_maxima),
                                  random.randint(cor_minima, cor_maxima),
                                  random.randint(cor_minima, cor_maxima))
                q.cor_atual    = (random.randint(cor_minima, cor_maxima),
                                  random.randint(cor_minima, cor_maxima),
                                  random.randint(cor_minima, cor_maxima))

                aleatorio = round(random.random(), 5)
                # --- Gerar filho ---
                if aleatorio < -(quantidade_quadrados / 100) + 1:
                    qu = Actor('quadrado.png')
                    qu.pos = random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)
                    qu.cor_atual = (
                        255,
                        255,
                        255,
                    )
                    qu.imagem_limpa = qu._surf.copy()
                    quadr.append(qu)
                    velocidade_y.append(5)
                    velocidade_x.append(5)

                elif aleatorio > quantidade_quadrados / 100:
                    if i < j:
                        quadr.pop(i)
                        quadr.pop(j - 1)
                        velocidade_x.pop(i)
                        velocidade_x.pop(j - 1)
                        velocidade_y.pop(i)
                        velocidade_y.pop(j - 1)
                    else:
                        quadr.pop(j)
                        quadr.pop(i - 1)
                        velocidade_x.pop(j)
                        velocidade_x.pop(i - 1)
                        velocidade_y.pop(j)
                        velocidade_y.pop(i - 1)

                # Registra cooldown para esse par
                pares_em_cooldown[par] = COOLDOWN_FRAMES

    quantidade_quadrados = len(quadr)
    contador += 1
    if contador % 60 == 0:
        print(f"({contador / 60}, {quantidade_quadrados})")

    if quantidade_quadrados == 2 or quantidade_quadrados <= 1:
        print(f"({round(contador / 60)}, {quantidade_quadrados})")
        print("F")
        print(f"Duração: {contador / 60} segundos")
        pygame.quit()
        sys.exit()

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