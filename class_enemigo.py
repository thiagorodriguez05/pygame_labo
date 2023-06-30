import pygame
from configuracion import rescalar_imagenes, obtener_rectangulo

class Personaje:
    
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
        # Configuración
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # Animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto_deidara"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        # Rectángulos
        rectangulo = self.animaciones["camina_derecha_deidara"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)
        self.velocidad = velocidad
    
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            rescalar_imagenes(self.animaciones[clave], self.ancho, self.alto)
    
    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
    
    
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
    
    def update(self, pantalla, piso, plataformas):
        if self.que_hace == "derecha_deidara":
            self.animar(pantalla, "camina_derecha_deidara")
            self.mover(self.velocidad)
        elif self.que_hace == "izquierda_deidara":
            self.animar(pantalla, "camina_izquierda_deidara")
            self.mover(-self.velocidad)
        elif self.que_hace == "quieto_deidara":
            self.animar(pantalla, "quieto_deidara")
        self.verificar_colisiones(plataformas)
    
    def verificar_colisiones(self, plataformas):
        for plataforma in plataformas:
            if self.lados["bottom"].colliderect(plataforma["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma["main"].top