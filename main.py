import pygame as pg
from PIL import Image, ImageDraw
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

hollow = False
px_lst = []

def random_rgb():
    colour = randint(122, 255), randint(122, 255), randint(122, 255)
    return colour

colour = random_rgb()

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

    global px_lst, colour
    px_lst = []

    for i in range(grid_num):

        px_lst.append([])

        if i <= (grid_num - 1)/2:
            for j in range(grid_num):
                px_lst[i].append(choice([0, 1])) # draw a pixel if 1 
        else:
            px_lst[i] = px_lst[(grid_num - 1) - i]

    colour = random_rgb()
    return px_lst

def render_pic(px_lst, cell_size, hollow = False):
    """
    :param list[][] px_lst: The randomly generated grid
    :param list cell_size: [grid_width, grid_length],the cell_size of one grid
    :param bool hollow: Whether the picture needs to be hollowed out
    :rtype: None
    """

    pos = [width/2 - cell_size*grid_num/2, 200 - cell_size*grid_num/2] # to center the icon on screen

    if not hollow:
        for i, col in enumerate(px_lst):
            for j, to_draw in enumerate(col): 
                # create rectangle on image
                if to_draw:
                    pg.draw.rect(screen, 
                                colour, 
                            [pos[0] + cell_size*i, pos[1] + cell_size*j] + [cell_size, cell_size])

    else:
        thick = 3
        r, g, b = colour
        
        for i, col in enumerate(px_lst):
            for j, to_draw in enumerate(col): 
                # create rectangle on image
                if to_draw:
                    # up direction
                    start_of_col = i == 0
                    if start_of_col or not px_lst[i - 1][j]:
                        pg.draw.line(screen, colour,
                        [pos[0] + cell_size * i, pos[1] + cell_size * j],
                        [pos[0] + cell_size * i, pos[1] + cell_size * (j + 1)],
                        thick)

                        # surf = pg.Surface()
                        # screen.blit()

                    # down direction
                    end_of_col = i == grid_num - 1
                    if end_of_col or not px_lst[i + 1][j]:
                        pg.draw.line(screen, colour,
                        [pos[0] + cell_size * (i + 1), pos[1] + cell_size * j],
                        [pos[0] + cell_size * (i + 1), pos[1] + cell_size * (j + 1)],
                        thick)

                    # left direction
                    start_of_row = j == 0
                    if start_of_row or not px_lst[i][j - 1]:
                        pg.draw.line(screen, colour,
                        [pos[0] + cell_size * i, pos[1] + cell_size * j],
                        [pos[0] + cell_size * (i + 1), pos[1] + cell_size * j],
                        thick)

                    # right direction
                    end_of_row =  j == grid_num - 1
                    if end_of_row or not px_lst[i][j + 1]:
                        pg.draw.line(screen, colour,
                        [pos[0] + cell_size * i, pos[1] + cell_size * (j + 1)],
                        [pos[0] + cell_size * (i + 1), pos[1] + cell_size * (j + 1)],
                        thick)

def save_pic(px_lst):
    """
    """

    size = 300, 300
    cell_l = size[0] / grid_num

    # creating new Image object
    img = Image.new("RGBA", size, (255, 255, 255, 0)) 
    # transparent cells are represented as (255, 255, 255, 0)

    for i, col in enumerate(px_lst):
        for j, to_draw in enumerate(col): 
            # create rectangle on image
            if to_draw:
                shape = [(cell_l * i, cell_l * j), (cell_l * (i + 1) - 0.5, cell_l * (j + 1) - 0.5)] 
                # (x0, y0), (x1, y1) or (x0, y0, x1, y1)
                draw = ImageDraw.Draw(img)
                draw.rectangle(shape, colour)

    img.save(f"pic/{randint(0,100)}.png")

def pic_change(new_pic = True):
    """
    Every time when the pic changes, the screen refreshes itself.
    """

    global px_lst

    write_txt([30, 380], 20, [255, 255, 255], 'consolas', "Refresh(r)")
    write_txt([30, 430], 20, [255, 255, 255], 'consolas', "Change size(c) current: {}x{}".format(grid_num, grid_num))
    write_txt([30, 480], 20, [255, 255, 255], 'consolas', "Save(s)")
    write_txt([30, 530], 20, [255, 255, 255], 'consolas', "Hollow(h) current:{}".format(str(hollow)))
    if new_pic:
        px_lst = refresh_pic(grid_num)
    render_pic(px_lst, cell_size, hollow)
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
                save_pic(px_lst)

            elif event.key == pg.K_h:
                hollow = not hollow
                pic_change(False)

            elif event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    clock.tick(60)