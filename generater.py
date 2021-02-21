from PIL import Image, ImageDraw
from random import choice, randint

def random_rgb():
	colour = randint(122, 255), randint(122, 255), randint(122, 255)
	return colour

def refresh_pic(grid_num):
    """
    :param int grid_num: an odd number of pixels of the grid
    :rtype: list[][]
    """

    px_lst = []

    for i in range(grid_num):

        px_lst.append([])

        if i <= (grid_num - 1)/2:
            for j in range(grid_num):
                px_lst[i].append(choice([0, 1])) # draw a pixel if 1 
        else:
            px_lst[i] = px_lst[(grid_num - 1) - i]

    return px_lst

def render_pic(img, px_lst, cell_l):
    """
    :param list[] px_lst: The randomly generated grid
    :param list pos: [x, y],the coor of the picture
    :param list size: [grid_width, grid_length],the size of one grid
    :rtype: None
    """

    colour = random_rgb()

    for i, col in enumerate(px_lst):
        for j, to_draw in enumerate(col): 
            # create rectangle on image
            if to_draw:
                shape = [(cell_l * i, cell_l * j), (cell_l * (i + 1) - 0.5, cell_l * (j + 1) - 0.5)] # (x0, y0), (x1, y1) or (x0, y0, x1, y1)
                # print((cell_l * i, cell_l * j), (cell_l * (i + 1), cell_l * (j + 1)))
                draw = ImageDraw.Draw(img)
                draw.rectangle(shape, colour)

def main(length, grid_num):
    size = length, length
    cell_l = length/grid_num

    # creating new Image object
    img = Image.new("RGBA", size, (255, 255, 255, 0)) # transparent cells are represented as (255, 255, 255, 0)

    px_lst = refresh_pic(grid_num)
    render_pic(img, px_lst, cell_l)
    img.save(f"temp/{length}_{grid_num}.png")

main(30, 8)