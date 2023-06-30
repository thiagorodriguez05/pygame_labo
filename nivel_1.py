import pygame
from nivel import*
from configuracion import*
from class_personaje import*

class nivelUno(nivel):
    def __init__(self, pantalla, personaje_principal, lista_plataforma, imagen_fondo):
        W = pantalla.get_width()
        H = pantalla.get_heigth()

        # FONDO
        fondo = pygame.image.load(r"MI_JUEGO\niveles\Orochimarus Base destroyed.png")
        fondo = pygame.transform.scale(fondo, (W,H))
        
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

        
        pygame.mixer.init()
        pygame.display.set_caption("Attack on Akatsuki")


        imagen_vida = pygame.image.load(r"MI_JUEGO\personaje\vida\0.png")
        imagen_vida = pygame.transform.scale(imagen_vida, (175, 60))
        
        # PISO
        piso = pygame.Rect(0, 0, W, 20)
        piso.top = mi_personaje.lados["main"].bottom
        lados_piso = obtener_rectangulo(piso)
        
        # Botón de inicio
        imagen_menu = pygame.image.load(r"MI_JUEGO\niveles\menu_juego2.png")
        imagen_menu = pygame.transform.scale(imagen_menu, TAMAÑO_PANTALLA)
        
        # Fuente de texto
        fuente = pygame.font.Font(None, 36)
        
        # Puntuación
        puntuacion = 0
        mostrar_rectangulos = False
        saltando = False
        
        super().__init__(pantalla, mi_personaje, fondo, lista_plataforma)
