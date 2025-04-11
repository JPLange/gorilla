import set_name
# from random import randint

def lets_play():
    set_names()
    # construct playingfield
    # kill greeter
    # make big frame with background picture
    field = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=100)
    field.grid(column=4, row=4, columnspan=20, rowspan=20)
    # choose random heights for towers
    # dependencies: random module
    # TODO Make towers of varying size, banana, later: sun, background picture
    # TODO for now only PLACEHOLDERS
    # add towers with correct hight, sun,
    # choose random positions for the two monkey, each on thier side of the map
    # place the monkeys
    # make a function for angle and power input query, should check for players turn
