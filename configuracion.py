import pygame
import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    
    return lista_girada

def rescalar_imagenes(lista_imagenes, W, H):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], (W, H))

def obtener_rectangulo(principal):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario
##########################################################

personaje_quieto = [pygame.image.load(r"MI_JUEGO\personaje\quieto\2.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\quieto\3.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\quieto\4.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\quieto\5.png")
                    ]

personaje_moviendose =  [pygame.image.load(r"MI_JUEGO\personaje\movimiento\6.png"),
                        pygame.image.load(r"MI_JUEGO\personaje\movimiento\7.png"),
                        pygame.image.load(r"MI_JUEGO\personaje\movimiento\8.png"),
                        pygame.image.load(r"MI_JUEGO\personaje\movimiento\9.png"),
                        pygame.image.load(r"MI_JUEGO\personaje\movimiento\10.png"),
                        pygame.image.load(r"MI_JUEGO\personaje\movimiento\11.png"),
                        pygame.image.load(r"MI_JUEGO\personaje\movimiento\12.png"),
                        pygame.image.load(r"MI_JUEGO\personaje\movimiento\13.png")
                        ]

personaje_moviendose_izquierda = girar_imagenes(personaje_moviendose, True, False)

personaje_salta =  [pygame.image.load(r"MI_JUEGO\personaje\salto\15.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\salto\16.png")]

atque_patada = [pygame.image.load(r"MI_JUEGO\personaje\ataque_1\31.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_1\32.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_1\33.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_1\34.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_1\35.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_1\36.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_1\37.png")]

ataque_puño = [pygame.image.load(r"MI_JUEGO\personaje\ataque_2\38.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_2\39.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_2\40.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_2\41.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_2\42.png")]

ataque_rasengan = [pygame.image.load(r"MI_JUEGO\personaje\ataque_3\43.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\44.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\45.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\46.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\48.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\49.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\50.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\51.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\52.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\53.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\54.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\55.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\56.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\57.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\58.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\59.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\60.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\61.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\62.png"),
                    pygame.image.load(r"MI_JUEGO\personaje\ataque_3\63.png")]

vida_personaje = [pygame.image.load(r"MI_JUEGO\personaje\vida\0.png")]

deidara_camina_derecha = [pygame.image.load(r"MI_JUEGO\enemigo\deidara\0.png"),
                    pygame.image.load(r"MI_JUEGO\enemigo\deidara\1.png"),
                    pygame.image.load(r"MI_JUEGO\enemigo\deidara\2.png"),
                    pygame.image.load(r"MI_JUEGO\enemigo\deidara\3.png"),
                    pygame.image.load(r"MI_JUEGO\enemigo\deidara\4.png"),
                    pygame.image.load(r"MI_JUEGO\enemigo\deidara\5.png")]

deidara_camina_izquierda = girar_imagenes(deidara_camina_derecha, True, False)