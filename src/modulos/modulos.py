# -*- coding: utf-8 -*-

from numbers import Real
import math


def euclidean_modulo(dividend: Real, divisor: Real) -> Real:
    """
    Euclidean modulo, output smallest positive remainder
    Note that, contrary to % operator or math.fmod function, remainder sign will not depend on either divisor or dividend

    For more information: https://en.wikipedia.org/wiki/Modulo_operation#Variants_of_the_definition

    This modulo verify these two formulas (with quotient as integer):

        dividend = divisor * quotient + remainder

        0 <= remainder <= abs(divisor)

    Args:
        dividend (Real)
        divisor (Real)

    Returns:
        remainder (Real) : result of the modulo operation
    """
    # quotient = int(dividend/divisor)
    return dividend - (abs(divisor) * math.floor(abs(dividend/divisor)))


def rounded_modulo(dividend: Real, divisor: Real) -> Real:
    """
    Rounded modulo operation, output centered remainder (i.e. closest to zero remainder)
    This is already the standard behavior for math.remainder for float values

    For more information: https://en.wikipedia.org/wiki/Modulo_operation#Variants_of_the_definition

    This modulo verify these two formulas (with quotient as integer):

        dividend = divisor * quotient + remainder

        -abs(divisor)/2 <= remainder <= abs(divisor)/2

    Args:
        dividend (Real)
        divisor (Real)

    Returns:
        remainder (Real) : result of the modulo operation
    """
    return dividend - (divisor * round(dividend/divisor))


def floored_modulo(dividend: Real, divisor: Real) -> Real:
    """
    Floored modulo operation, output remainder where quotient is defined by flooring (always rounded downwards)
    This is already the standard behavior for % symbol on integers values
    Note that remainder sign will be same as divisor

    For more information: https://en.wikipedia.org/wiki/Modulo_operation#Variants_of_the_definition

    This modulo verify these the formula (with quotient as integer):

        remainder = dividend - quotient * floor(dividend/quotient)

    Args:
        dividend (Real)
        divisor (Real)

    Returns:
        remainder (Real) : result of the modulo operation
    """
    return dividend - (divisor * math.floor(dividend/divisor))


def ceiled_modulo(dividend: Real, divisor: Real) -> Real:
    """
    Ceiled modulo operation, output remainder where quotient is defined by ceiling (always rounded upwards)
    Note that remainder sign will be the opposite of divisor sign

    For more information: https://en.wikipedia.org/wiki/Modulo_operation#Variants_of_the_definition

    This modulo verify these the formula (with quotient as integer):

        remainder = dividend - quotient * ceil(dividend/quotient)

    Args:
        dividend (Real)
        divisor (Real)

    Returns:
        remainder (Real) : result of the modulo operation
    """
    return dividend - (divisor * math.ceil(dividend/divisor))


def truncated_modulo(dividend: Real, divisor: Real) -> Real:
    """
    Truncated modulo operation, output remainder where quotient is defined by truncation
    This is already the standard behavior for math.fmod
    Note that remainder sign will be same as dividend

    For more information: https://en.wikipedia.org/wiki/Modulo_operation#Variants_of_the_definition

    This modulo verify these the formula (with quotient as integer):

        remainder = dividend - quotient * trunc(dividend/quotient)

    Args:
        dividend (Real)
        divisor (Real)

    Returns:
        remainder (Real) : result of the modulo operation
    """
    # For truncation, we need to first cast to float value, because not all Real values support __trunc__ method
    return dividend - (divisor * math.trunc(float(dividend/divisor)))
