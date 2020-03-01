import itertools
from random import choice

poss_values = [0, 1, 2] # paper is 0; rock is 1; scissors is 2

poss_combs = [combination for combination in itertools.product(poss_values, repeat=3)]
combs_dict = dict.fromkeys(poss_combs, 0)

attempts = 0
score = 0
user_inputs = []

while True:
    computer_choice = 0
    if attempts < 4:
        computer_choice = choice([0, 1, 2])
    else:
        # paper is 0; rock is 1; scissors is 2
        if combs_dict[user_inputs[-2], user_inputs[-1], 0] > combs_dict[user_inputs[-2], user_inputs[-1], 1] and combs_dict[user_inputs[-2], user_inputs[-1], '0'] > combs_dict[user_inputs[-2], user_inputs[-1], '2']:
            computer_choice = 0
        elif combs_dict[user_inputs[-2], user_inputs[-1], 1] > combs_dict[user_inputs[-2], user_inputs[-1], 0] and combs_dict[user_inputs[-2], user_inputs[-1], 1] > combs_dict[user_inputs[-2], user_inputs[-1], 2]:
            computer_choice = 1
        else:
            computer_choice = 2

    print("Please, choose 0 or 1 or 2")
    user_inp = input()
    print("Computer prediction: ", computer_choice)
    if computer_choice == user_inp:
        print("Computer is right.")
        score += 1
    else:
        print("Computer is wrong.")
        score -= 1
    attempts += 1
    print("Current score is: ", score)

    user_inputs.append(user_inp)
    if len(user_inputs) > 3:
        combs_dict[tuple(user_inputs[-3:])] += 1