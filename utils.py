import random


def dice_roll(dice_pool, modifier, dt):

    success = 'https://gcdnb.pbrd.co/images/aPlfABvAX3kP.png'
    fail = 'https://gcdnb.pbrd.co/images/yevrCWBNRc0c.png'
    critical = 'https://gcdnb.pbrd.co/images/Ht05rykRt9Ay.png'
    disaster = 'https://gcdnb.pbrd.co/images/sryNUnTV6AKc.png'

    if dice_pool != 0:
        dice_rolled = random.sample(range(1, 21), dice_pool)
        used_roll = max(dice_rolled)
    else:
        dice_rolled = random.sample(range(1, 21), 2)
        used_roll = min(dice_rolled)

    final_roll = used_roll + modifier

    if final_roll >= dt and used_roll == 20:
        test_result = critical
        color = 0x492ea4
        result_text = 'Sucesso Crítico!'
    elif final_roll >= dt:
        test_result = success
        color = 0xd1a533
        result_text = 'Sucesso.'
    elif final_roll < dt and used_roll == 1:
        test_result = disaster
        color = 0x000000
        result_text = 'Falha Crítica!'
    else:
        test_result = fail
        color = 0x981111
        result_text = 'Falha.'

    #reply = f'**Dice -** {dice_rolled} | **You rolled -** {final_roll} vs {dt} | **[{test_result}]**'

    return dice_rolled,used_roll,test_result,color,result_text,used_roll
