# import pygame
# class Button:
#     def __init__(self, x, y, image_path, callback=None):
#         self.rect = pygame.Rect(x, y, 0, 0)
#         self.image = pygame.image.load(image_path)
#         self.rect.width = self.image.get_width()
#         self.rect.height = self.image.get_height()
#         self.callback = callback

#     def draw(self, screen):
#         screen.blit(self.image, self.rect)

#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             if self.rect.collidepoint(event.pos):
#                 if self.callback is not None:
#                     self.callback()