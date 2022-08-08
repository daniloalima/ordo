import random


def dice_roll(dice_pool, modifier, dt):

    if dice_pool != 0:
        dice_rolled = random.sample(range(1, 20), dice_pool)
        used_roll = max(dice_rolled)
    else:
        dice_rolled = random.sample(range(1, 20), 2)
        used_roll = min(dice_rolled)

    final_roll = used_roll + modifier

    if final_roll >= dt and used_roll == 20:
        test_result = 'Critical! <:sucesso_critico:969977872401977354>'
    elif final_roll >= dt:
        test_result = 'Sucess! <:sucesso_normal:969976778363912283>'
    elif final_roll < dt and used_roll == 1:
        test_result = 'Disaster! <:falha_critica:969976778204520448>'
    else:
        test_result = 'Fail! <:falha_normal:969976778326159390>'

    reply = f'**Dice -** {dice_rolled} | **You rolled -** {final_roll} vs {dt} | **[{test_result}]**'

    return reply
