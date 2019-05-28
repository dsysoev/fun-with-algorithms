# test random

import random

num_topics, num_themes = 1000, 2

lst = [random.randint(0, num_themes - 1) for i in range(num_topics)]

with open('input.txt', 'w') as f:
    f.write("{} {}\n".format(num_topics, num_themes))
    for l in lst:
        f.write(str(l) + '\n')
