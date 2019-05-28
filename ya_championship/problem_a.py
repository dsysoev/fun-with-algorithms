# -*- coding: utf-8 -*-

# A. Лента рекомендаций
# Рассмотрим ленту рекомендаций разнородного контента.
# В ней смешаны объекты разного типа (картинки, видео, новости и т.д.).
# Эти объекты обычно упорядочиваются по релевантности:
# чем релевантнее (интереснее) объект пользователю,
# тем он ближе к началу списка рекомендаций.
# При таком упорядочивании в списке рекомендаций часто встречается несколько объектов одного типа подряд.
# Рекомендации кажутся однообразными и поэтому не нравятся пользователям.
# Необходимо реализовать алгоритм, который по списку рекомендаций составит
# новый список — лишённый этого недостатка и при этом максимально релевантный.

# Пусть задан исходный список рекомендаций a = [a0, a1, a2, ..., an] длиной n > 0.
# Объект под номером i имеет тип с номером bi = (0, ..., m-1) и релевантность r(ai) = 2 ^ -i
# Рассмотрим список, который получается из исходного выбором подмножества объектов и их перестановкой:
# x = [ai0, ai1, ..., aik-1] длины k (1 <= k <= n).
# Список называется допустимым, если никакие два подряд идущих объекта в нем не совпадают по типу, т.е.
# bi != bi+1 для всех j = 0,... k-2.
# Релевантность списка вычисляется по формуле ∑ 2 ^ -j * r(aij).
# Вам нужно найти максимальный по релевантности список среди всех допустимых.

# recomendation list           [a0, a1, a2, ..., an]; n in (0 - N)
# theme for each recomendation [b0, b1, b2, ..., bn]; b in (0 - M)
# relevance of topic r(ai) = 2 ^ -i
# relevance of list Sum (2 ^ -j) * r(aij)

def group_topics(topics, num_themes):

    lst = [[] for _ in range(num_themes)]
    # group topics by themes
    for item in topics:
        lst[themes[item]].append(item)

    return lst

def themes_to_topics(list_themes, topics, themes, num_themes):

    # convert topics to groups
    g_topics = group_topics(topics, num_themes)

    list_view = []
    for one_view in list_themes:
        # set initial dict for storing index
        dindex = {i: 0 for i in range(num_themes)}

        view = []
        for index in one_view:
            # add first element from topics for selected theme
            view.append(g_topics[index][dindex[index]])
            # increase index
            dindex[index] += 1

        list_view.append(view)

    return list_view

def algorithm(lst, aval_themes):

    on_depth = False

    l_lst = []
    for elem, l_aval_themes in zip(lst, aval_themes):

        for i1, _ in enumerate(l_aval_themes):
            current_themes = l_aval_themes[:]

            prev = None
            if len(elem) > 0:
                prev = elem[-1]

            if current_themes[i1] > 0 and prev != i1:
                # check we have theme and prev theme != theme
                on_depth = True
                current_themes[i1] -= 1
                v = algorithm([elem + (i1, )], [current_themes])
                l_lst.extend(v)

    # on the max depth
    if not on_depth:
        # return source list
        return lst

    return l_lst

def relevance(lst, themes):

    summ = 0
    prev_t = None

    for i, indx in enumerate(lst):
        # num theme
        t = themes[indx]
        # restriction if prev theme == theme
        rule = float('-Inf') if t == prev_t else 0
        prev_t = t
        # importance
        summ += (2 ^ -i) * (2 ^ -i) + rule

    return summ

def main(topics, themes, num_themes):

    # create list with number topics for each theme
    count_themes = [len(x) for x in group_topics(topics, num_themes)]

    # get list of all combinations
    combinations = algorithm([()], [count_themes])

    # convert combinations to topics
    all_view = themes_to_topics(combinations, topics, themes, num_themes)

    # calculate relevance
    relevance_list = [relevance(x, themes) for x in all_view]

    # select list with max relevance
    max_index = relevance_list.index(max(relevance_list))

    return all_view[max_index], relevance_list[max_index]

if __name__ in '__main__':

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    len_list, count_themes = lines[0].strip().split()

    themes = [int(x.strip()) for x in lines[1:] if x.strip() != '']
    topics = list(range(int(len_list)))

    best_list, max_relevance = main(topics, themes, int(count_themes))

    with open('output.txt', 'w') as f:
        f.write(' '.join([str(x) for x in best_list]))
        
    print(best_list)
