import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def random_number(min_number,max_number):
    return random.randint(min_number,max_number)

def gamea(player_choose):
    objects = '$stone','$scissors','$paper'
    robot_choose = objects[random.randint(0,2)]
    if player_choose == '$stone' and robot_choose == '$paper' or player_choose == '$scissors' and robot_choose == '$stone' or player_choose == '$paper' and robot_choose == '$scissors':
        return 'robot win. He chose a',robot_choose
    elif robot_choose == player_choose:
        return 'draw.bot chose a',robot_choose
    else:
        return 'you win.bot chose a',robot_choose
print(gamea('$stone'))