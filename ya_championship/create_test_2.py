# test 2
# correct answer
# [0, 3, 1, 4, 2, 6, 5]

num_topics, num_themes = 10, 2

lst = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1]

with open('input.txt', 'w') as f:
    f.write("{} {}\n".format(num_topics, num_themes))
    for l in lst:
        f.write(str(l) + '\n')
