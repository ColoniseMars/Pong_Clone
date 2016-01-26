import pygame
def draw_img(screen, pos, path):
    """Draws an image"""
    Texture = pygame.image.load(path)
    screen.blit(Texture, pos)

def draw_img_trans(screen, pos, path, colorkey = (255,0,255)):
    """Draws and image with transparacy, colorkey is the color that will be transparant"""
    Texture = pygame.image.load(path).convert()
    Texture.set_colorkey(colorkey)
    screen.blit(Texture, pos)

def draw_text(screen, pos, text, font = None, font_color = (255,255,255), font_size = 30):
    """Draws text"""
    #font = pygame.font.SysFont(font, font_size)
    textrender = pygame.font.SysFont(font, font_size).render(text, 1, font_color)
    screen.blit(textrender, pos)