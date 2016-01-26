import pygame
import BallClass
import Texture
import config


bar_texture_path = "textures/bar.png" 
ball_texture_path = "textures/ball.png"
bgcolor = (0,0,0)

bar_texture = pygame.image.load(bar_texture_path)
ball_texture = pygame.image.load(ball_texture_path)
size_ball = ball_texture.get_rect().size
size_bar = bar_texture.get_rect().size

def do_tick(pos):
    if (BallClass.ball.pos[0]-(size_ball[0]/2) <100 or BallClass.ball.pos[0]+(size_ball[0]/2)>1400) and (BallClass.ball.pos[1]-(size_ball[1]/2) <pos[1] or BallClass.ball.pos[1]+(size_ball[1]/2)>pos[1]+config.window_height):
        BallClass.ball.normal_bounce("vertical")
        BallClass.ball.normal_bounce("horizontal")
    elif BallClass.ball.pos[0]-(size_ball[0]/2) <100 or BallClass.ball.pos[0]+(size_ball[0]/2)>1400:
        BallClass.ball.normal_bounce("vertical")
    elif BallClass.ball.pos[1]-(size_ball[1]/2) <0 or BallClass.ball.pos[1]+(size_ball[1]/2) >1000:
        BallClass.ball.normal_bounce("horizontal")
    BallClass.ball.move()


    #print(str(BallClass.ball.pos))
    #print("did tick")

def draw(screen, pos):
    do_tick(pos)
    screen.fill(bgcolor)
    posball = BallClass.ball.pos

    screen.blit(ball_texture, (posball[0]-size_ball[0], posball[1]-size_ball[1]))

    mousepos = pygame.mouse.get_pos()
    barpos = (config.window_width-100, mousepos[1] - size_bar[1]/2)
    if barpos[1] <0:
        barpos = (barpos[0], 0)
    elif barpos[1] + size_bar[1] > config.window_height:
        barpos = (barpos[0], config.window_height-size_bar[1])
    screen.blit(bar_texture, barpos)
    
    
    #Texture.draw_text(screen, (0,0), str(BallClass.ball.angle))

    #print("printed graphics")