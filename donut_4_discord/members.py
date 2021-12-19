import random
from dotenv import load_dotenv
import os

# Env Variables
load_dotenv()
BOT_NAME = os.getenv('BOT_NAME')
BOT_USER_ID = int(os.getenv('BOT_USER_ID'))
ADMIN_NAME = os.getenv('ADMIN_NAME')
ADMIN_USER_ID = int(os.getenv('ADMIN_USER_ID'))

bot_name_id = (BOT_NAME, BOT_USER_ID)
admin_name_id = (ADMIN_NAME, ADMIN_USER_ID)

def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)

def get_pairs(members_names_ids):

    if bot_name_id in members_names_ids:
        members_names_ids.remove(bot_name_id)

    pairs = []

    while len(members_names_ids) > 1:
        rand1 = pop_random(members_names_ids)
        print(rand1)
        rand2 = pop_random(members_names_ids)
        print(rand2)
        pair = rand1, rand2
        pairs.append(pair)

    # If odd number, peyton gets 2 meetings
    if len(members_names_ids) == 1 and members_names_ids[0] != admin_name_id:
        pairs.append((members_names_ids[0], admin_name_id))
    elif len(members_names_ids) == 1 and members_names_ids[0] == admin_name_id:
        # TODO: DM admin to let them know they won't have a match.
        pass

    return pairs




