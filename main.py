import pygame as pg
from random import choice, randint
from sys import exit

pg.init()
width = 500
height = 600
screen = pg.display.set_mode([width, height], pg.RESIZABLE)
pg.display.set_caption("Github icon generator")
title_icon = pg.image.load("title_icon.png")
pg.display.set_icon(title_icon)
clock = pg.time.Clock()

grid_num = 9
cell_size = int(width/2/grid_num)

def write_txt(pos, size, color, font, info):
    """
    """

    ft = pg.font.SysFont(font,cell_size)
    text = ft.render(info, True, color)
    screen.blit(text, pos)

def refresh_pic(grid_num):
    """
    :param int grid_num: an odd number of pixels of the grid
    :rtype: list[][]
    """

    px_lst = []

    rdm_cl = [randint(0, 255), randint(0, 255), randint(0, 255)]
    px_cl = [[0, 0, 0], rdm_cl]

    for i in range(grid_num):
        px_lst.append([])

    for i in range(len(px_lst)):

        if i <= (grid_num-1)/2:
            for j in range(grid_num):
                px_lst[i].append(choice(px_cl))
        else:
            px_lst[i] = px_lst[(grid_num-1) - i]

    return px_lst

def render_pic(px_lst, cell_size):
    """
    :param list[][] px_lst: The randomly generated grid
    :param list pos: [x, y],the coor of the picture
    :param list cell_size: [grid_width, grid_length],the cell_size of one grid
    :rtype: None
    """

    pos = [width/2 - cell_size*grid_num/2, 200 - cell_size*grid_num/2]

    for i, col in enumerate(px_lst):
        for j, colour in enumerate(col):
            pg.draw.rect(screen, 
                         colour, 
                         [pos[0] + cell_size*i, pos[1] + cell_size*j] + [cell_size, cell_size])

def save_pic(px_lst):
    """
    """

    pass

def pic_change():
    write_txt([30, 400], 20, [255, 255, 255], 'consolas', "Refresh(r)")
    write_txt([30, 460], 20, [255, 255, 255], 'consolas', "Change size(c) current: {}x{}".format(grid_num, grid_num))
    write_txt([30, 520], 20, [255, 255, 255], 'consolas', "Save(s)")
    px_lst = refresh_pic(grid_num)
    render_pic(px_lst, cell_size)
    pg.display.update()
    screen.fill((0, 0, 0))

pic_change()

while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.VIDEORESIZE:
            screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            width = event.w
            height = event.h
            pic_change()

        elif event.type == pg.KEYDOWN:

            if event.key == pg.K_r:
                pic_change()

            elif event.key == pg.K_c:
                if grid_num < 11:
                    grid_num += 2
                else:
                    grid_num = 5

                pic_change()

            elif event.key == pg.K_s:
                print("save")

            elif event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    clock.tick(60)