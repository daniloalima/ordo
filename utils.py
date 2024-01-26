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

if __name__ == '__main__':
    result = dice_roll(3, 9)
    print(result)