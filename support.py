"""Module created by TerraBoii where you can find some useful functions."""


def rlc(amount=2, limit=100):
    """Creates list with random numbers (from 1 to limit that is given by user(default is 100) in it.
    Amount of elements is given by the user, default is 2.
    rlc -> random list creator"""
    lst = []
    from random import randint as rng
    for counter in range(0, amount):
        number = rng(1, limit)
        lst.append(number)
    return lst


def _gcd(_list: list[int]):
    """This function can find Greatest Common Divisor of multiple numbers"""
    answer = 1  # Is our answer, if it isn`t changed then it will be 1
    divisors = []  # Is a container for our divisors will be expended
    smallest = min(_list)
    result = []
    for runner in range(1, int(smallest ** (1 / 2)) + 1):
        if smallest % runner == 0:
            result.append(runner)
    support = []  # This list is used to store another divisors
    for runner in result:
        support.append(int(smallest / runner))
    if support[-1] == smallest ** (1 / 2):
        support.pop()
    result.extend(support)
    result = sorted(list(set(result)))
    divisors.extend(result)
    for divisor in divisors:
        counter = 0
        for element in _list:
            if element % divisor == 0:
                counter += 1
            if counter == len(_list) and divisor > answer:
                answer = divisor
    return answer
