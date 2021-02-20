import pygame as pg
import random
from sys import exit

pg.init()
size = width, height = 600, 600
screen = pg.display.set_mode(size, pg.RESIZABLE)
pg.display.set_caption("Github icon generator")
clock = pg.time.Clock()
# title_icon = pg.image.load("some random picture.png")
fclock = pg.time.Clock()

def write_txt(pos, size, color, font, info):
    """
    """
    ft = pg.font.SysFont(font, size)
    text = ft.render(info, True, color)
    screen.blit(text, pos)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.e:
                pg.quit()
                exit()
            elif event.key == pg.K_RIGHT:
                pass
            elif event.key == pg.K_UP:
                pass
            elif event.key == pg.K_DOWN:
                pass
            elif event.key == pg.K_ESCAPE:
                exit()
        elif event.type == pg.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pg.display.set_mode(size, pg.RESIZABLE)

    pg.display.update()
    screen.fill((0, 0, 0))
    clock.tick(60)