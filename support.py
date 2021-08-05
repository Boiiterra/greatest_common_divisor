"""Module created by TerraBoii for generating random elements based on amount and max number"""


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


def all_divisors(number: int):
    """Returns list of every divisor given number has."""
    result = []
    for runner in range(1, int(number ** (1 / 2)) + 1):
        if number % runner == 0:
            result.append(runner)
    support = []  # This list is used to store another divisors
    for runner in result:
        support.append(int(number / runner))
    if support[-1] == number ** (1 / 2):
        support.pop()
    result.extend(support)
    result = sorted(list(set(result)))
    return result


def _gcd(_list: list[int]):
    """This function can find Greatest Common Divisor of multiple numbers, new"""
    answer = 1  # Is our answer, if it isn`t changed then it will be 1
    divisors = []  # Is a container for our divisors will be expended
    for element in _list:  # Going through list
        result = []
        for runner in range(1, int(element ** (1 / 2)) + 1):
            if element % runner == 0:
                result.append(runner)
        support = []  # This list is used to store another divisors
        for runner in result:
            support.append(int(element / runner))
        if support[-1] == element ** (1 / 2):
            support.pop()
        result.extend(support)
        result = sorted(list(set(result)))
        print(result)
        divisors.extend(result)
    for _divisor in set(divisors):  # Using convertor to get rid of clones and to be faster
        if divisors.count(_divisor) == len(_list) and answer < _divisor:  # Checking if we need to change the answer
            answer = _divisor
    return answer
    # TODO: make it faster
