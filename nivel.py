import pygame
import sys
from modo import *

def iniciar_juego():
    global JUEGO_INICIADO
    JUEGO_INICIADO = True
    # Código para iniciar el juego aquí
    print("Iniciando juego...")

JUEGO_INICIADO = False

class Plataforma:
    def __init__(self, imagen, rectangulo, lados):
        self.imagen = imagen
        self.rectangulo = rectangulo
        self.lados = lados

class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo):
        self.pantalla = pantalla
        self.jugador = personaje_principal
        self.lista_plataformas = []

        for plataforma in lista_plataformas:
            imagen = pygame.image.load(plataforma["imagen"]).convert_alpha()
            imagen = pygame.transform.scale(imagen, (300, 50))
            rectangulo = plataforma["rectangulo"]
            lados = plataforma["lados"]
            nueva_plataforma = Plataforma(imagen, rectangulo, lados)
            self.lista_plataformas.append(nueva_plataforma)

        self.imagen_fondo = imagen_fondo

    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Botón izquierdo del ratón
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if not JUEGO_INICIADO:
                        if 700 < mouse_x < 1100 and 300 < mouse_y < 500:
                            iniciar_juego()

        self.actualizar_pantalla()
        self.leer_inputs()

    def actualizar_pantalla(self):
        self.pantalla.blit(self.imagen_fondo, (0, 0))
        self.jugador.update(self.pantalla, self.lista_plataformas)

        for plataforma in self.lista_plataformas:
            self.pantalla.blit(plataforma.imagen, plataforma.rectangulo)
            if mostrar_rectangulos:
                for lado in plataforma.lados:
                    pygame.draw.rect(self.pantalla, "Red", plataforma.lados[lado], 4)

    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.jugador.que_hace = "derecha"
        elif keys[pygame.K_a]:
            self.jugador.que_hace = "izquierda"
        elif keys[pygame.K_w]:
            self.jugador.que_hace = "salta"
        elif keys[pygame.K_i]:
            self.jugador.que_hace = "patada"
        elif keys[pygame.K_j]:
            self.jugador.que_hace = "puño"
        elif keys[pygame.K_l]:
            self.jugador.que_hace = "rasengan"
        else:
            self.jugador.que_hace = "quieto"

    def dibujar_rectangulos(self):
        if not JUEGO_INICIADO:
            self.pantalla.blit(imagen_menu, (0, 0))
        else:
            self.actualizar_pantalla(self.pantalla, self.jugador, self.imagen_fondo, self.lista_plataformas, mostrar_rectangulos)

            # Dibujar rectángulos de colisión de plataformas y personaje
            if mostrar_rectangulos:
                for plataforma in self.lista_plataformas:
                    for lado in plataforma.lados:
                        pygame.draw.rect(self.pantalla, "Red", plataforma.lados[lado], 4)
                        pygame.draw.rect(self.pantalla, "Red", plataforma.rectangulo, 4)
                for lado in lados_piso:
                    pygame.draw.rect(self.pantalla, "Blue", lados_piso[lado], 3)
                for lado in self.jugador.lados:
                    pygame.draw.rect(self.pantalla, "Orange", self.jugador.lados[lado], 3)

            # Dibujar rectángulos de colisión de plataformas y personaje
            if mostrar_rectangulos:
                for plataforma in self.lista_plataformas:
                    for lado in plataforma["lados"]:
                        pygame.draw.rect(self.pantalla, "Red", plataforma["lados"][lado], 4)
                        pygame.draw.rect(self.pantalla, "Red", plataforma["rectangulo"], 4)
                for lado in lados_piso:
                    pygame.draw.rect(self.pantalla, "Blue", lados_piso[lado], 3)
                for lado in self.jugador.lados:
                    pygame.draw.rect(self.pantalla, "Orange", self.jugador.lados[lado], 3)