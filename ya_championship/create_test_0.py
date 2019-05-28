# test 0
# correct answer
# [0]

num_topics, num_themes = 1, 1

lst = [0]

with open('input.txt', 'w') as f:
    f.write("{} {}\n".format(num_topics, num_themes))
    for l in lst:
        f.write(str(l) + '\n')
