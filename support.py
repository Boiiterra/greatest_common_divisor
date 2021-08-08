"""Module created by TerraBoii where you can find some useful functions."""


def int_list_creator(amount=2, limit=100):
    """Creates list with random numbers (from 1 to limit that is given by user, default is 100.
    Amount of elements is given by the user, default is 2."""
    lst = []  # List that is going to store generated numbers
    from random import randint as rng  # importing randint for integer generation
    for counter in range(0, amount):  # populating list using for loop
        number = rng(1, limit)
        lst.append(number)
    return lst


def _gcd(_list: list[int]):
    """This function can find Greatest Common Divisor of multiple numbers, as argument takes list with integers."""
    answer = 0  # This variable is going to store gcd
    divisors = []  # Is a container for our divisors, will be expended
    smallest = min(_list)  # To make this function faster we will find every divisor the smallest has
    for number in range(1, int(smallest ** (1 / 2)) + 1):  # Using square method to find divisors
        if smallest % number == 0:
            divisors.append(number)
    support = []  # This list is used to store another divisors
    for divisor in divisors:  # Here we use first list of divisors to finish full one
        support.append(int(smallest / divisor))
    divisors.extend(support)  # Finishing list with adding last divisors
    divisors = sorted(list(set(divisors)), reverse=True)  # Deleting clones and making list reversed
    _list.pop(_list.index(smallest))  # Deleting smallest element because we know all it's divisors
    for divisor in divisors:  # in this block we are looking for greatest common divisor
        counter = 0  # This variable used to count how many element could be divided by divisor
        for element in _list:
            if element % divisor == 0:
                counter += 1
        else:  # When we finished going through list given by user we check if we need to change the gcd
            if counter == len(_list):  # Checking if we need to change the answer and ending loop
                answer = divisor
                break
    return answer
