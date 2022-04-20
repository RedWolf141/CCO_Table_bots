import random

def change_ts(ts):
    k = 0
    for x in range(ts):
        a = random.randint(1,10)
        if a == 1 or a == 2:
            k += 1
    return ts + k


    