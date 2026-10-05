import random
import statistics

# 1. Randomly pick heads or tails
# 2. Add a point to the respective variable (e.g.  heads_count / tails_count)
# 3. Repeat the number of times written in the function
# 4. Return the percentage of heads and tails
def flip_coin(count):
    heads_count = 0
    tails_count = 0
    # 3. Repeat the number of times written in the function
    for x in range(count):
        # 1. randomly pick heads or tails
        result = random.choice(["heads", "tails"])
        # 2. add a point to the respective variable (heads_count / tails_count)
        if result == "heads":
            heads_count += 1
        if result == "tails":
            tails_count += 1
    # 4. Return the percentage of heads and tails
    heads_procentage = (heads_count / count) * 100
    tails_procentage = (tails_count / count) * 100
    diff_from50 = abs(heads_procentage - 50)
    return heads_procentage, tails_procentage, diff_from50
count = 1
for x in range(10):
    differences = []
    for y in range(10):
        _, _, difference = flip_coin(count)
        differences.append(difference)
    average = statistics.mean(differences)
    print(count, average)
    count *= 10