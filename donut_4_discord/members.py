import random


def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)

def get_pairs(members):

    members.remove('🍩🤖')

    pairs = []
    print("HERE", members)
    while len(members) > 1:
        rand1 = pop_random(members)
        print(rand1)
        rand2 = pop_random(members)
        print(rand2)
        pair = rand1, rand2
        pairs.append(pair)

    # If odd number, peyton gets 2 meetings
    if len(members) == 1 and members[0] != 'peyton':
        pairs.append((members[0], 'peyton'))

    return pairs


if __name__ == '__main__':
    toy_members = ['tay', 'joe', 'mo', 'tier', 'alex', 'caro', 'grant']
    toy_df = pd.DataFrame({'members': toy_members})

    out = get_pairs(toy_members)




