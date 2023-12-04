def cut_rod(price: list[int], length: int) -> float:
    """ simplest cut rod algorithm
        return value of maximum income
    """
    if length == 0:
        return 0
    income = float("-Inf")
    for i in range(length):
        # recursive call for rod with a shorter length (n - i - 1)
        income = max(income, price[i] + cut_rod(price, length - i - 1))
    return income


def memoized_cut_rod(price: list[int], length: int) -> float:
    """ cut rod algorithm with memoized income """
    incomelst = [float("-Inf") for _ in range(length + 1)]
    # set zero income for zero length
    incomelst[0] = 0
    return memoized_cut_rod_aux(price, length, incomelst)


def memoized_cut_rod_aux(price: list[int],
                         length: int,
                         incomelst: list[float]) -> float:
    """ recursive cut rod algorithm with memoized income values """
    if incomelst[length] >= 0:
        # if the calculation was performed earlier
        # return income value for current length
        return incomelst[length]

    income = float("-Inf")
    for i in range(length):
        income = max(income, price[i] +
                     memoized_cut_rod_aux(price, length - i - 1, incomelst))
    incomelst[length] = income
    return income


def bottom_up_cut_rod(price: list[int], length: int) -> float:
    """ bottom up implementation of cut rod memoized algorithm """
    incomelst = [float("-Inf") for _ in range(length + 1)]
    # set zero income for zero length
    incomelst[0] = 0
    for j in range(1, length + 1):
        income = float("-Inf")
        for i in range(j):
            income = max(income, price[i] + incomelst[j - i - 1])
        # set income for current length
        incomelst[j] = income
    # income for whole rod
    return incomelst[length]


def ext_bottom_up_cut_rod(price: list[int],
                          length: int) -> tuple[list[float], list[int]]:
    """ bottom up implementation of cut rod memoized algorithm """
    incomelst = [float("-Inf") for _ in range(length + 1)]
    cutlst = [0 for _ in range(length + 1)]
    # set zero income for zero length
    incomelst[0] = 0
    for j in range(1, length + 1):
        income = float("-Inf")
        for i in range(j):
            if income < price[i] + incomelst[j - i - 1]:
                income = price[i] + incomelst[j - i - 1]
                cutlst[j] = i + 1
        # set income for current length
        incomelst[j] = income
    # income for whole rod
    return incomelst, cutlst


def print_cut_rod(price: list[int], length: int) -> str:
    _, cutlst = ext_bottom_up_cut_rod(price, length)
    num = int(length)
    lst = []
    while num > 0:
        lst.append(str(cutlst[num]))
        num -= cutlst[num]
    return '(' + ", ".join(lst) + ')'


def main() -> None:
    # price for length
    # length:1  2  3  4  5   6   7   8   9   10
    price = [1, 5, 8, 9, 10, 17, 17, 20, 25, 30]
    # rod length
    rod = 7
    print('simple cut rod   :', cut_rod(price, rod))
    print('memoized cut rod :', memoized_cut_rod(price, rod))
    print('bottom up cut rod:', bottom_up_cut_rod(price, rod))
    print('optimal cutting of the rod:', print_cut_rod(price, rod))
    print('optimal cutting of the rod:', print_cut_rod(price, rod))


if __name__ in '__main__':
    main()
