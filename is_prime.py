#!/usr/bin/env python3

import math
from typing import Union


def is_prime(value: Union[int, float]) -> bool:
    """
    Test whether a number is a prime number.

    This function accepts both integers and floats but the float must
    not have a decimal value.

    Args:
        value: Value to test for primality.

    Returns: boolian

    """

    # Check the input
    if isinstance(value, float):
        if not value.is_integer():
            raise ValueError('Input value is a non-integer float.')

    # Force to int
    int_val = int(value)

    # Check edge cases
    if int_val < 0:
        raise ValueError('The primality of negative integers is undefined.')

    elif int_val == 0:
        raise ValueError('The primality of zero is undefined.')

    elif int_val == 1:
        return False

    elif int_val == 2:
        return True

    elif int_val == 3:
        return True

    elif int_val % 2 == 0:
        return False

    # Determine the maximum denominator to test
    max_denominator = min(int_val, math.ceil(math.sqrt(int_val)) + 2)

    # Exhaustively tests input with odd numbers
    return __prime_checker__(int_val,  max_denominator)


def __prime_checker__(test_value: int, max_denominator: int) -> bool:
    """
    helper function to test prime numbers

    """
    for i in range(3, max_denominator, 2):
        if test_value % i == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    # Command line usage

    import argparse
    parser = argparse.ArgumentParser(description='Test primality of a number')
    parser.add_argument('number', metavar='integer', type=int,
                        help='Integer to test for primality')

    number = parser.parse_args().number
    print(is_prime(number))
