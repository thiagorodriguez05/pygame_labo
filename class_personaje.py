import pygame
from configuracion import rescalar_imagenes, obtener_rectangulo

class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
        # Configuración
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # Gravedad
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        self.desplazamiento_y = 0
        # Animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        # Rectángulos
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
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
    
    def update(self, pantalla, piso):
        if self.que_hace == "derecha":
            if not self.esta_saltando:
                self.animar(pantalla, "camina_derecha")
            self.mover(self.velocidad)
        elif self.que_hace == "izquierda":
            if not self.esta_saltando:
                self.animar(pantalla, "camina_izquierda")
            self.mover(-self.velocidad)
        elif self.que_hace == "salta":
            if not self.esta_saltando:
                self.esta_saltando = True
                self.desplazamiento_y = self.potencia_salto
        elif self.que_hace == "quieto":
            if not self.esta_saltando:
                self.animar(pantalla, "quieto")
        elif self.que_hace == "patada":
            if not self.esta_saltando:
                self.animar(pantalla, "ataque_patada")
            self.mover(self.velocidad)
        elif self.que_hace == "puño":
            if not self.esta_saltando:
                self.animar(pantalla, "ataque_puño")
            self.mover(self.velocidad)
        elif self.que_hace == "rasengan":
            if not self.esta_saltando:
                self.animar(pantalla, "ataque_rasengan")
            self.mover(self.velocidad)
        
        self.aplicar_gravedad(pantalla, piso)
    
    
    def aplicar_gravedad(self, pantalla, piso):
        if self.esta_saltando:
            self.animar(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top 