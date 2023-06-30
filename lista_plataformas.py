import pygame
from imagenes import obtener_rectangulo
lista_plataformas = [
    {
        "imagen": pygame.image.load(r"MI_JUEGO\niveles\nivel_1.png"),
        "rectangulo": pygame.Rect(500, 620, 300, 50),
        "lados": obtener_rectangulo(pygame.Rect(500, 620, 300, 50))
    },
    {
        "imagen": pygame.image.load(r"MI_JUEGO\niveles\nivel_1.png"),
        "rectangulo": pygame.Rect(820, 620, 300, 50),
        "lados": obtener_rectangulo(pygame.Rect(200, 100, 300, 50))
    }
]

for plataforma in lista_plataformas:
    plataforma["imagen"] = pygame.transform.scale(plataforma["imagen"], (200, 50))