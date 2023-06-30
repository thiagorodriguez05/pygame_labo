import pygame
import sys
from configuracion import *
from class_personaje import Personaje
from modo import *
from class_plataformas import Plataforma


def actualizar_pantalla(pantalla, un_personaje, fondo, lista_plataformas, lista_objetos, mostrar_rectangulos):
    pantalla.blit(fondo, (0, 0))

    un_personaje.update(pantalla, lados_piso)

    for plataforma in lista_plataformas:
        pantalla.blit(plataforma["imagen"], plataforma["rectangulo"])
        if mostrar_rectangulos:
            for lado in plataforma["lados"]:
                pygame.draw.rect(pantalla, "Red", plataforma["lados"][lado], 4)

    for objeto in lista_objetos:
        pantalla.blit(objeto["imagen"], objeto["rectangulo"])


def iniciar_juego():
    global JUEGO_INICIADO
    JUEGO_INICIADO = True
    # Código para iniciar el juego aquí
    print("Iniciando juego...")


# CONFIGURACION
W, H = 1800, 900  # Nuevas dimensiones de la ventana
TAMAÑO_PANTALLA = (W, H)
FPS = 18
pygame.init()
pygame.mixer.init()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Attack on Akatsuki")
RELOJ = pygame.time.Clock()
JUEGO_INICIADO = False

# FONDO
fondo = pygame.image.load(r"MI_JUEGO\niveles\Orochimarus Base destroyed.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

# PERSONAJE
posicion_inicial = (H / 2 - 300, 650)
tamaño = (75, 85)

diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_moviendose
diccionario_animaciones["camina_izquierda"] = girar_imagenes(personaje_moviendose, True, False)
diccionario_animaciones["ataque_patada"] = atque_patada
diccionario_animaciones["ataque_puño"] = ataque_puño
diccionario_animaciones["ataque_rasengan"] = ataque_rasengan

velocidad = 10
mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, velocidad)

imagen_vida = pygame.image.load(r"MI_JUEGO\personaje\vida\0.png")
imagen_vida = pygame.transform.scale(imagen_vida, (175, 60))

# PISO
piso = pygame.Rect(0, 0, W, 20)
piso.top = mi_personaje.lados["main"].bottom
lados_piso = obtener_rectangulo(piso)

lista_plataformas = [
    {
        "imagen": pygame.image.load(r"MI_JUEGO\niveles\nivel_1.png").convert_alpha(),
        "rectangulo": pygame.Rect(500, 600, 300, 50),
        "lados": {}
    },
    {
        "imagen": pygame.image.load(r"MI_JUEGO\niveles\nivel_1.png").convert_alpha(),
        "rectangulo": pygame.Rect(900, 600, 300, 50),
        "lados": {}
    }
]

plataformas = []  # Lista para almacenar las instancias de las plataformas

for plataforma in lista_plataformas:
    imagen = plataforma["imagen"]
    rectangulo = plataforma["rectangulo"]
    instancia_plataforma = Plataforma(imagen, rectangulo)
    plataformas.append(instancia_plataforma)


lista_objetos = [
    {
        "imagen": pygame.image.load(r"MI_JUEGO\objetos\0.png"),
        "rectangulo": pygame.Rect(1450, 830, 100, 100),
        "lados": obtener_rectangulo(pygame.Rect(0, 0, 100, 100))
    }
]

for objetos in lista_objetos:
    objetos["imagen"] = pygame.transform.scale(objetos["imagen"], (50, 50))


# Botón de inicio
imagen_menu = pygame.image.load(r"MI_JUEGO\niveles\menu_juego2.png")
imagen_menu = pygame.transform.scale(imagen_menu, TAMAÑO_PANTALLA)

# Fuente de texto
fuente = pygame.font.Font(None, 36)

# Puntuación
puntuacion = 0
mostrar_rectangulos = False
saltando = False

while True:
    RELOJ.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                mostrar_rectangulos = not mostrar_rectangulos
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo del ratón
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if not JUEGO_INICIADO:
                    if 700 < mouse_x < 1100 and 300 < mouse_y < 500:
                        iniciar_juego()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and mi_personaje.lados["main"].x < W - velocidad - mi_personaje.ancho:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_a] and mi_personaje.lados["main"].x > mi_personaje.velocidad:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_w]:
        mi_personaje.que_hace = "salta"
    elif keys[pygame.K_i]:
        mi_personaje.que_hace = "patada"
    elif keys[pygame.K_j]:
        mi_personaje.que_hace = "puño"
    elif keys[pygame.K_l]:
        mi_personaje.que_hace = "rasengan"
    else:
        mi_personaje.que_hace = "quieto"

    if not JUEGO_INICIADO:
        PANTALLA.blit(imagen_menu, (0, 0))
    else:
        actualizar_pantalla(PANTALLA, mi_personaje, fondo, lista_plataformas, lista_objetos, mostrar_rectangulos)
        PANTALLA.blit(imagen_vida, (10, 10))

        # Dibujar rectángulos de colisión de plataformas y personaje
        if mostrar_rectangulos:
            for plataforma in lista_plataformas:
                for lado in plataforma["lados"]:
                    pygame.draw.rect(PANTALLA, "Red", plataforma["lados"][lado], 4)
                    pygame.draw.rect(PANTALLA, "Red", plataforma["rectangulo"], 4)
            for lado in lados_piso:
                pygame.draw.rect(PANTALLA, "Blue", lados_piso[lado], 3)
            for lado in mi_personaje.lados:
                pygame.draw.rect(PANTALLA, "Orange", mi_personaje.lados[lado], 3)

    pygame.display.update()