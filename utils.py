import random


def dice_roll(dice_pool, modifier, dt=None):

    if dice_pool != 0:
        dice_rolled = random.sample(range(1, 21), dice_pool)
        used_roll = max(dice_rolled)
    else:
        dice_rolled = random.sample(range(1, 21), 2)
        used_roll = min(dice_rolled)

    final_roll = used_roll + modifier
    dice_rolled.sort()

    if dt is not None:
        dt_result = check_dt(dt, used_roll, final_roll)
        return dice_rolled, final_roll, dt_result[0], dt_result[1]

    return dice_rolled, final_roll

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
    result = dice_roll(5, 10, 15)
    print(result)