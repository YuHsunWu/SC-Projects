"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    data_width = width // len(YEARS)
    x_coordinate = data_width * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x+GRAPH_MARGIN_SIZE, 0, x+GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
        canvas.create_text(x+GRAPH_MARGIN_SIZE+5, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+5, text=YEARS[i],
                           anchor=tkinter.NW, font='times 10')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    data_width = CANVAS_WIDTH // len(YEARS)
    name_order = 0
    # Different names have their own loop
    for name in lookup_names:
        year_order = 0
        # To define the index of the list: rank_list, so that we can find y1
        rank1_list_order = 0
        # To define the index of the list: rank_list, but finding y2 instead
        rank2_list_order = 0
        # We can grab year and rank data in these two lists respectively.
        # Indexes in these two lists should be corresponding
        year_list = []
        rank_list = []
        # This for loop appends all data appeared in a specific name
        for year, rank in name_data[name].items():
            year_list.append(year)
            rank_list.append(rank)
        # the_year means the year we are checking now
        # This for loop deals with the line for a specific year, namely the_year,
        # and the following year, namely next_year.
        for the_year in YEARS:
            # Have Not yet reached the last year in YEARS
            if year_order < len(YEARS)-1:
                year_order += 1
                next_year = YEARS[year_order]
            # Reached the last year in YEARS
            else:
                next_year = YEARS[len(YEARS)-1]

            x1 = get_x_coordinate(CANVAS_WIDTH, year_order - 1) + GRAPH_MARGIN_SIZE
            x2 = get_x_coordinate(CANVAS_WIDTH, year_order) + GRAPH_MARGIN_SIZE

            # We encounter 4 situations here: (the_year in YEARS, or not) * (next_year in YEARS, or not)
            if str(the_year) in year_list:
                rank1 = rank_list[rank1_list_order]
                # the rank ranges from 1 to 1000, but the CANVAS_HEIGHT may be less than 1000,
                # thus I allocate the height in proportion
                y1 = int((int(rank1)) * (CANVAS_HEIGHT / 1000)+GRAPH_MARGIN_SIZE)
                rank1_list_order += 1
                if str(next_year) in year_list:
                    rank2_list_order += 1
                    # In addition, we have to consider if next_year is the last year in YEARS
                    if rank2_list_order < len(rank_list):
                        rank2 = rank_list[rank2_list_order]
                        y2 = int((int(rank2)) * (CANVAS_HEIGHT / 1000) + GRAPH_MARGIN_SIZE)
                    else:
                        canvas.create_text(x1 + data_width + TEXT_DX, y1, text=str(name) + ' ' + str(rank1),
                                           fill=COLORS[name_order % len(COLORS)], anchor=tkinter.SW, font='times 10')
                # If that year has no ranking in next_year, y2 aligns with the visible bottom line of the canvas
                else:
                    rank2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    y2 = rank2
            # If that name has no ranking in the_year, y1 aligns with the visible bottom line of the canvas
            else:
                rank1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                y1 = rank1
                if str(next_year) in year_list:
                    if rank2_list_order < len(rank_list)-1:
                        rank2 = rank_list[rank2_list_order]
                        y2 = int((int(rank2)) * (CANVAS_HEIGHT / 1000) + GRAPH_MARGIN_SIZE)
                    else:
                        canvas.create_text(x1 + data_width + TEXT_DX, y1, text=str(name) + ' ' + str(rank1),
                                           fill=COLORS[name_order % len(COLORS)], anchor=tkinter.SW, font='times 10')
                else:
                    rank2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    y2 = rank2
            # Draw the line and the text after getting 4 locations needed,
            # except for the situation that next_year becomes the last year in YEARS
            if rank2_list_order <= len(rank_list)-1:
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[name_order % len(COLORS)])
                if y1 < CANVAS_HEIGHT - GRAPH_MARGIN_SIZE:
                    canvas.create_text(x1+TEXT_DX, y1, text=str(name) + ' ' + str(rank1),
                                    fill=COLORS[name_order % len(COLORS)], anchor=tkinter.SW, font='times 10')
                else:
                    canvas.create_text(x1 + TEXT_DX, y1, text=str(name) + '*',
                                       fill=COLORS[name_order % len(COLORS)], anchor=tkinter.SW, font='times 10')
        # Start checking the next name in the next loop
        name_order += 1

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
