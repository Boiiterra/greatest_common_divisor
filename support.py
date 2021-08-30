"""Module created by TerraBoii where you can find some useful functions."""


def every_divisor(integer: int):
    """Finds all divisors given number has."""
    divisors = []
    for number in range(1, int(integer ** (1 / 2)) + 1):  # Using square method to find divisors
        if integer % number == 0:
            divisors.append(number)
    support = []
    for divisor in divisors:  # Here we use first list of divisors to finish full one
        support.append(int(integer / divisor))
    divisors.extend(support)  # Finishing list with adding last divisors
    return sorted(list(set(divisors)), reverse=True)  # Deleting clones and making list reversed


def _gcd(_list: list[int]):
    """This function can find Greatest Common Divisor of multiple numbers, as argument takes list with integers."""
    divisors = every_divisor(min(_list))  # We will find every divisor of the smallest number in the list
    _list.pop(_list.index(min(_list)))  # Deleting smallest element because we know all it's divisors
    for divisor in divisors:  # in this block we are looking for greatest common divisor
        counter = 0
        for element in _list:
            if element % divisor == 0:
                counter += 1
            else:
                break
        else:  # When we finished going through list given by user we check if we need to change the gcd
            if counter == len(_list):  # Checking if we need to change the answer and ending loop
                return divisor
