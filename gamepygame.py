import pygame
import random
import sys
from gtts import gTTS
import os

# Inicializando o Pygame
pygame.init()

# Definindo algumas cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definindo as configurações da janela
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60

# Criando a janela do jogo
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Digite a Palavra")

# Carregando a fonte
font = pygame.font.Font(None, 48)

# Carregando sons
acerto_som = pygame.mixer.Sound("./success-1-6297.mp3")
erro_som = pygame.mixer.Sound("./buzzer-or-wrong-answer-20582.mp3")

# Lista de imagens
image_path_banana = "./banana.png"
image_banana = pygame.image.load(image_path_banana)
image_banana = pygame.transform.scale(image_banana, (300, 150))

image_path_livro = "./livro.png"
image_livro = pygame.image.load(image_path_livro)
image_livro = pygame.transform.scale(image_livro, (300, 150))

image_path_sol = "./sol.png"
image_sol = pygame.image.load(image_path_sol)
image_sol = pygame.transform.scale(image_sol, (300, 150))

image_path_cachorro = "./cachorro.png"
image_cachorro = pygame.image.load(image_path_cachorro)
image_cachorro = pygame.transform.scale(image_cachorro, (300, 150))

image_path_gato = "./gato.png"
image_gato = pygame.image.load(image_path_gato)
image_gato = pygame.transform.scale(image_gato, (300, 150))

image_path_carro = "./carro.png"
image_carro = pygame.image.load(image_path_carro)
image_carro = pygame.transform.scale(image_carro, (300, 150))

image_path_lapis = "./lapis.png"
image_lapis = pygame.image.load(image_path_lapis)
image_lapis = pygame.transform.scale(image_lapis, (300, 150))

image_path_bolas = "./bolas.png"
image_bolas = pygame.image.load(image_path_bolas)
image_bolas = pygame.transform.scale(image_bolas, (300, 150))

image_path_radio = "./radio.png"
image_radio = pygame.image.load(image_path_radio)
image_radio = pygame.transform.scale(image_radio, (300, 150))

image_path_amor = "./amor.png"
image_amor = pygame.image.load(image_path_amor)
image_amor = pygame.transform.scale(image_amor, (300, 150))

image_path_comer = "./comer.png"
image_comer = pygame.image.load(image_path_comer)
image_comer = pygame.transform.scale(image_comer, (300, 150))

image_path_nadar = "./nadar.png"
image_nadar = pygame.image.load(image_path_nadar)
image_nadar = pygame.transform.scale(image_nadar, (300, 150))

image_path_casar = "./casar.png"
image_casar = pygame.image.load(image_path_casar)
image_casar = pygame.transform.scale(image_casar, (300, 150))

image_path_pular = "./pular.png"
image_pular = pygame.image.load(image_path_pular)
image_pular = pygame.transform.scale(image_pular, (300, 150))

image_path_rato = "./rato.png"
image_rato = pygame.image.load(image_path_rato)
image_rato = pygame.transform.scale(image_rato, (300, 150))

image_path_linha = "./linha.png"
image_linha = pygame.image.load(image_path_linha)
image_linha = pygame.transform.scale(image_linha, (300, 150))

# Lista de palavras e imagens
dicio = {
    "banana": image_banana,
    "sol": image_sol,
    "cachorro": image_cachorro,
    "livro": image_livro,
    "gato": image_gato,
    "carro": image_carro,
    "lapis": image_lapis,
    "bolas": image_bolas,
    "radio": image_radio,
    "amor": image_amor,
    "comer": image_comer,
    "nadar": image_nadar,
    "casar": image_casar,
    "pular": image_pular,
    "rato": image_rato,
    "linha": image_linha
}
palavras = list(dicio.keys())

# Posições das letras faltantes
posicoes = {
    "banana": [4, 5],
    "sol": [2],
    "cachorro": [5, 6],
    "livro": [3, 4],
    "gato": [0, 1],
    "carro": [2, 3],
    "lapis": [0, 1],
    "bolas": [0, 1],
    "radio": [0, 1],
    "amor": [2, 3],
    "comer": [0, 1],
    "nadar": [0, 1],
    "casar": [2, 3],
    "pular": [2, 3],
    "rato": [0, 1],
    "linha": [0, 1]
}

# Criar diretório de áudios, se não existir
if not os.path.exists('audios'):
    os.makedirs('audios')

# Função para criar áudio da palavra
def criar_audio(palavra):
    tts = gTTS(text=palavra, lang='pt')
    filename = os.path.join('audios', f"{palavra}.mp3")
    tts.save(filename)
    return filename

# Função para tocar áudio da palavra
def tocar_audio(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

# Variável global para rastrear a palavra atual
indice_palavra = 0

# Função para exibir a próxima palavra na lista
def proxima_palavra():
    global indice_palavra
    palavra = palavras[indice_palavra]
    palavra_modificada = list(palavra)
    letras_faltantes = []
    for pos in posicoes[palavra]:
        letras_faltantes.append(palavra[pos])
        palavra_modificada[pos] = '_'
    indice_palavra = (indice_palavra + 1) % len(palavras)
    return "".join(palavra_modificada), letras_faltantes, palavra

# Função para desenhar o texto na tela
def desenhar_texto(texto, x, y, cor=BLACK):
    texto_surface = font.render(texto, True, cor)
    texto_rect = texto_surface.get_rect(center=(x, y))
    screen.blit(texto_surface, texto_rect)

# Função principal do jogo
def main():
    palavra_atual, letras_faltantes, palavra_completa = proxima_palavra()
    input_text = ""
    score = 0
    palavra_revelada = False

    # Criar e tocar áudio da palavra
    audio_file = criar_audio(palavra_completa)

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        # Desenha a palavra atual na tela com '_'
        desenhar_texto(palavra_atual, WIDTH // 2, HEIGHT // 2)

        # Desenha o texto de entrada na tela
        desenhar_texto(input_text, WIDTH // 2, HEIGHT // 2 + 50)

        # Desenha a pontuação na tela
        desenhar_texto(f"Score: {score}", WIDTH // 2, 50)

        # Desenha a imagem correspondente
        screen.blit(dicio[palavra_completa], (WIDTH / 3, HEIGHT // 6))

        pygame.display.flip()

        # Verifica eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == "".join(letras_faltantes):
                        score += 1
                        acerto_som.play()
                        palavra_revelada = True
                    else:
                        erro_som.play()

        # Exibir palavra completa e tocar áudio se revelada
        if palavra_revelada:
            desenhar_texto(palavra_completa, WIDTH // 2, HEIGHT // 2 + 150)
            if not pygame.mixer.music.get_busy():
                tocar_audio(audio_file)
                palavra_revelada = False

                # Gera uma nova palavra após acerto
                palavra_atual, letras_faltantes, palavra_completa = proxima_palavra()
                # Criar e tocar áudio da nova palavra
                audio_file = criar_audio(palavra_completa)
                tocar_audio(audio_file)
                input_text = ""

        clock.tick(FPS)

if __name__ == "__main__":
    main()
