import os

default_model = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
some_move_model = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]


def print_board(model):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tic Tac Toe\n")
    print("   |   |   ")
    print(" " + model[0] + " | " + model[1] + " | " + model[2] + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + model[3] + " | " + model[4] + " | " + model[5] + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + model[6] + " | " + model[7] + " | " + model[8] + " ")
    print("   |   |   ")


def mark_move(move, marker, model):
    pos = int(move)
    if pos == 1:
        pos = 6
    elif pos == 2:
        pos = 7
    elif pos == 3:
        pos = 8
    elif pos == 4:
        pos = 3
    elif pos == 5:
        pos = 4
    elif pos == 6:
        pos = 5
    elif pos == 7:
        pos = 0
    elif pos == 8:
        pos = 1
    elif pos == 9:
        pos = 2

    print(str(pos))
    model[pos] = marker


def check_if_win(model, marker):
    ret = False
    if model[0:3] == [marker] * 3:
        ret = True
    elif model[3:6] == [marker] * 3:
        ret = True
    elif model[6:9] == [marker] * 3:
        ret = True
    elif model[0::3] == [marker] * 3:
        ret = True
    elif model[1::3] == [marker] * 3:
        ret = True
    elif model[2::3] == [marker] * 3:
        ret = True
    elif model[0] == model[4] and model[4] == model[8] and model[8] == marker:
        ret = True
    elif model[2] == model[4] and model[4] == model[6] and model[6] == marker:
        ret = True
    return ret


def check_if_draw(mod):
    if " " not in mod:
        return True
    else:
        return False


print_board(default_model)
player1_marker = "X"
player2_marker = "O"
model = default_model.copy()

while True:
    #print("\n")
    move = input("\nPlayer1 move: ")
    mark_move(move, player1_marker, model)
    print_board(model)
    if check_if_win(model, player1_marker):
        print("\nPlayer1 WIN!")
        break
    if check_if_draw(model):
        print("\nDraw")
        break

    move = input("\nPlayer2 move: ")
    mark_move(move, player2_marker, model)
    print_board(model)
    if check_if_win(model, player2_marker):
        print("\nPlayer2 WIN!")
        break
    if check_if_draw(model):
        print("\nDraw")
        break


