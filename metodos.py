import pygame
class imagen:
    def __init__(self, tamaño, origen, path_imagen):
        #self.imagen = pygame.Surface(tamaño)
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, tamaño)
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.center = origen
        self.sonido_colision = pygame.mixer.Sound("CLASE_16\ñam.mp3")
        self.sonido_colision.set_volume(0.5)
    
    def mover_imagen(self, sentido: str, desplazamiento: int, tamaño_pantalla: tuple):
        if sentido == "vertical":
            self.rectangulo.y += desplazamiento
            if self.rectangulo.top > tamaño_pantalla[1]:
                self.rectangulo.bottom = 0
        else:
            self.rectangulo.x += desplazamiento
            if self.rectangulo.left > tamaño_pantalla[0]:
                self.rectangulo.right = 0
    
    def detectar_colision(self, otra_imagen):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.sonido_colision.play()