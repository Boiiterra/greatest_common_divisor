"""Module created by TerraBoii where you can find some useful functions."""


def int_list_creator(amount=2, limit=100):
    """Creates list with random numbers (from 1 to limit that is given by user, default is 100.
    Amount of elements is given by the user, default is 2."""
    from random import randint as rng  # importing randint for integer generation
    return [rng(1, limit) for _ in range(amount)]  # Returning list with random ints in it based on given arguments


def _gcd(_list: list[int]):
    """This function can find Greatest Common Divisor of multiple numbers, as argument takes list with integers."""
    answer = 0
    divisors = []
    smallest = min(_list)  # To make this function faster we will find every divisor of the smallest number in the list
    for number in range(1, int(smallest ** (1 / 2)) + 1):  # Using square method to find divisors
        if smallest % number == 0:
            divisors.append(number)
    support = []
    for divisor in divisors:  # Here we use first list of divisors to finish full one
        support.append(int(smallest / divisor))
    divisors.extend(support)  # Finishing list with adding last divisors
    divisors = sorted(list(set(divisors)), reverse=True)  # Deleting clones and making list reversed
    _list.pop(_list.index(smallest))  # Deleting smallest element because we know it's divisors
    for divisor in divisors:  # in this block we are looking for greatest common divisor
        counter = 0
        for element in _list:
            if element % divisor == 0:
                counter += 1
        else:  # When we finished going through list given by user we check if we need to change the gcd
            if counter == len(_list):  # Checking if we need to change the answer and ending loop
                answer = divisor
                break
    return answer
