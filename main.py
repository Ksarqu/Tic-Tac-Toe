from os import system, path
from os import name as os_detection
from json import load, dump
from time import sleep

# loading language files

if not path.isfile("config.json"):
    with open("config.json", "w") as f:
        dump({"lang":"EN"}, f)
    print("look at new 'config.json' file, you can select between PL\EN")
    sleep(2)
    exit()
else:
    with open("config.json", "r") as f:
        configData = load(f)
    lang_file = "{}.json".format(configData["lang"])
    with open(f"languages/{lang_file}", "r") as f:
        language = load(f)


# Os detection
clear = None
if os_detection == "posix":
    clear = "clear"
elif os_detection == "nt":
    clear = "cls"
else:
    print("Your os is unsupported, Contact me to solve this")
    sleep(2)
    exit()

table = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
}
X_or_O = True


def check():
    for char in ["X", "O"]:
        if table[1] == char and table[2] == char and table[3] == char:
            return char
        elif table[4] == char and table[5] == char and table[6] == char:
            return char
        elif table[7] == char and table[8] == char and table[9] == char:
            return char
        elif table[1] == char and table[5] == char and table[9] == char:
            return char
        elif table[7] == char and table[5] == char and table[3] == char:
            return char
        elif table[1] == char and table[4] == char and table[7] == char:
            return char
        elif table[2] == char and table[5] == char and table[8] == char:
            return char
        elif table[3] == char and table[6] == char and table[9] == char:
            return char
        counter = 0
        for i in range(len(table)):
            if table[i + 1] != " ":
                counter = counter + 1
                if counter == 9:
                    return language["nobody"]


def game(table):
    print(f"""
      1 | 2 | 3
    1 {table[1]} | {table[2]} | {table[3]}  3
    4 {table[4]} | {table[5]} | {table[6]}  6
    7 {table[7]} | {table[8]} | {table[9]}  9
      7 | 8 | 9
    {language["whats_the_next_move"]}
    """)


while True:
    system(clear)
    game(table)
    if X_or_O:
        print(language["now_its_X_move"])
        letter = "X"
        X_or_O = False
    else:
        print(language["now_its_O_move"])
        letter = "O"
        X_or_O = True
    loop = True
    while loop:
        move = int(input(">>>"))
        if 1 <= move <= 9:
            if table[move] == " ":
                loop = False
            else:
                print(language["wrong_move"])
        else:
            print(language["wrong_move"])
    table.update([(move, letter)])
    result = check()
    if result is not None:
        if "X" or "O" in result:
            system(clear)
            print(language["winner"] + ": " + result)
            break
