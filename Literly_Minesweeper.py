# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:10:39 2019

@author: theod
"""
from numpy import empty
from random import randint

exit_args = ["off", "Off", "quit", "Quit", "exit", "Exit"]

def is_bomb(gam, x_, y_):
    pass

def build_bomb(x_, y_, nbomb_):
    if nbomb == x_*y_:
        raise Exception("Congratz, bud. All is bomb, you win")
    if nbomb > (x_)*(y_):
        raise Exception("Buddy, I know you're ambitious, but we just can't fit this many bombs here")
    bombs_ret = empty((ydim + 1, xdim + 1), bool)
    bombs_ret.fill(False)

    while nbomb_ > 0:
        xplace = randint(1,x_)
        yplace = randint(1,y_)
        if bombs_ret[yplace,xplace]:
            continue
        bombs_ret[yplace,xplace] = True
        nbomb_ -= 1

    return bombs_ret


arg_act = input("Welcome to shitty minesweeper, press enter to start\n")
if arg_act == "dev_mode":
    dev_mode = True
else:
    dev_mode = False
    instruct = input("do you want instructions? [y/n]")

    if instruct == "y":
        print("""
aight kiddo, buckle up.
You get a minefield, and ya wanna find the bombs.
If you think there's a bomb somewhere, say that you wanna
flag it by entering [flag x_coord y_coord]. If you wanna see
what is under the tile enter [check x_coord, y_coord].
If you check a bomb, you die.

If you think you've flagged all the bombs, just enter win and C4 urself ;)
""")

if dev_mode:
    xdim = 5
    ydim = 5
    nbomb = 3
else:
    xdim = int(input("How broad? "))
    ydim = int(input("How tall? "))
    nbomb = int(input("How many bombs? "))

game = empty((ydim + 1, xdim + 1), str)
game.fill("\u2586")

for i in range(xdim):
    j=i+1
    game[0,i+1] = j
    if i < ydim:
        game[i+1,0] = j
game[0,0] = ":)"

bombs = build_bomb(xdim, ydim, nbomb)
if dev_mode:
    dev_bombs = bombs.astype(int)
    for i in range(xdim):
        j=i+1
        dev_bombs[0,i+1] = j
        if i < ydim:
            dev_bombs[i+1,0] = j
    dev_bombs[0,0] = 0

    print(dev_bombs, "lol dev mode bomb layout")

#while arg_act != "off" and arg_act != ["off"] and arg_act != ["quit"]:
def main(arg_act = "on"):
    while arg_act not in exit_args:
        print(game)
        inp = input("what do, boss? \n")
        if inp in exit_args:
            return
        elif inp == "win":
            f_count = 0
            for i in range(xdim):
                for j in range(ydim):
                    if bombs[j, i] and game[j, i] != "F":
                        print("nope, you lose, nerd")
                        return
                    if game[j, i] == "F":
                        f_count += 1
            if f_count > nbomb:
                print("Looks like you had a bit too many flags there ;)")
            print("congratz, u win")
            if nbomb == 0:
                print("(even though you didn't even try)")
            return


        elif len(inp.split()) == 3:
            arg_act, arg_x, arg_y = inp.split()
            arg_x, arg_y = int(arg_x), int(arg_y)

            if arg_x <= 0 or arg_x > xdim or arg_y <= 0 or arg_y > ydim:
                print("woah there, buddy. Those coordinates are kinda out of bounds")
                continue

            if arg_act == "check":
                if game[arg_y, arg_x] == "F":
                    sure = input("You have a flag here, are you sure? [y/n]")
                    if sure != "y":
                        continue
                if bombs[arg_y, arg_x]:
                    print ("ooopsies, you hit a bomb, u ded")
                    return
                else:
                    game[arg_y, arg_x] = bombs[arg_y-1:arg_y+2, arg_x-1:arg_x+2].sum()

            elif arg_act == "flag":
                game[arg_y, arg_x] = "F"

main()

print("buhbaaay")