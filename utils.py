import random


def dice_roll(dice_pool, difficulty=None):
    difficulty = 6 if difficulty is None else difficulty
    dice_rolled = []
    sucess = 0

    for n in range(0, dice_pool):
        dice_rolled.append(random.randint(1, 10))

    dice_rolled.sort(reverse=True)

    for i in range(len(dice_rolled)):
        if dice_rolled[i] < difficulty:
            dice_rolled[i] = f'~~{dice_rolled[i]}~~'
        elif dice_rolled[i] == 10:
            dice_rolled[i] = f'**{dice_rolled[i]}**'
            sucess += 1
        elif dice_rolled[i] == 1:
            dice_rolled[i] = f'**~~{dice_rolled[i]}~~**'
        else:
            dice_rolled[i] = f'{dice_rolled[i]}'
            sucess += 1

    return dice_rolled, sucess

def check_dt(dt, used_roll, final_roll):
    dt_check_result = []
    if final_roll >= dt and used_roll == 20:
        dt_check_result.append(0x492ea4)
        dt_check_result.append('Sucesso Crítico!')
    elif final_roll >= dt:
        dt_check_result.append(0xd1a533)
        dt_check_result.append('Sucesso.')
    elif final_roll < dt and used_roll == 1:
        dt_check_result.append(0x000000)
        dt_check_result.append('Falha Crítica!')
    else:
        dt_check_result.append(0x981111)
        dt_check_result.append('Falha.')

    return dt_check_result

if __name__ == '__main__':
    result = dice_roll(3, 9)
    print(result)