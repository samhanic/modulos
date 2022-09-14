# -*- coding: utf-8 -*-

from decimal import Decimal as Decimal
from numbers import Real
import math
import platform

import numpy as np
import pytest

from modulos.modulos import euclidean_modulo, rounded_modulo, floored_modulo, ceiled_modulo, truncated_modulo

##### Setups #####

values_test_positive = [
                55,
                3,
                2,
                6.66,
                math.pi,
                987654321.987654321,
                Decimal(1),
                Decimal("3.58"),
                Decimal("39411.6811"),
                np.int8(25),
                np.int8(7),
                np.uint8(14),
                np.uint8(254),
                np.int16(2022),
                np.int16(499),
                np.int32(92312),
                np.int64(3534621),
                np.float16(155.364),
                np.float32(65842.5520),
                np.float64(14786322.1453223),
                np.float64(31672848.9421418)
              ]

if platform.system() != 'Windows':
    # Float128 is not available in windows, but we still want to test it to verify precision of operation within Linux
    values_test_positive.append(np.float128(14656199198.348697452122))
    values_test_positive.append(np.float128(64792397544.778624631336))

test_combinations = []

def construct_test_combinations():
    if not test_combinations:
        # Construct test values (both positive and negative numbers)
        values_test = []
        for value in values_test_positive:
            values_test.append(value)
            values_test.append(-value)

        # Construct test values combinations
        for dividend in values_test:
            for divisor in values_test:
                test_combinations.append({"dividend":dividend,"divisor":divisor})


def modulo_equations(dividend: Real, divisor: Real, remainder: Real):
    quotient = round((dividend-remainder)/divisor)

    if (isinstance(divisor, float) or isinstance(dividend, float) or isinstance(remainder, float)):
        # For float values, we need to verify equality dividend = divisor * quotient + remainder with approximate equality only
        return (math.isclose(dividend, divisor * quotient + remainder, rel_tol=1e-06) and (abs(remainder) < abs(divisor)))

    return ((dividend == divisor * quotient + remainder) and (abs(remainder) < abs(divisor)))

def are_same_sign(a, b):
    if (a == 0) or (b == 0):
        return True
    elif a > 0:
        return b > 0
    else:
        return b < 0

#### Euclidean modulo tests #####

def euclidean_modulo_combination_test(dividend, divisor):
        # We don't test incompatible types operation, as described in README
        try:
            dividend/divisor
            dividend < divisor
        except:
            return

        remainder = euclidean_modulo(dividend, divisor)

        # Assert basic modulo equations
        assert modulo_equations(dividend, divisor, remainder)

        # Assert result is always the closest to 0 positive
        assert((remainder >= 0) and (remainder < abs(divisor)))

        # Assert same output type to one of two inputs type
        assert((type(dividend) is type(remainder)) or (type(divisor is type(remainder))))
        return


def test_euclidean_modulo():
    construct_test_combinations()
    for values in test_combinations:
        euclidean_modulo_combination_test(values["dividend"], values["divisor"])


#### Rounded modulo tests #####

def rounded_modulo_combination_test(dividend, divisor):
        # We don't test incompatible types operation, as described in README
        try:
            dividend/divisor
            dividend < divisor
        except:
            return

        remainder = rounded_modulo(dividend, divisor)

        # Assert basic modulo equations
        assert modulo_equations(dividend, divisor, remainder)

        # Assert result is always the closest to 0
        assert(2*abs(remainder) <= abs(divisor))

        # Assert math.remainder shows same float output as this function
        assert(math.isclose(remainder, math.remainder(dividend, divisor), rel_tol=1e-05))

        # Assert same output type to one of two inputs type
        assert((type(dividend) is type(remainder)) or (type(divisor is type(remainder))))
        return


def test_rounded_modulo():
    construct_test_combinations()
    for values in test_combinations:
        rounded_modulo_combination_test(values["dividend"], values["divisor"])


#### Floored modulo tests #####

def floored_modulo_combination_test(dividend, divisor):
        # We don't test incompatible types operation, as described in README
        try:
            dividend/divisor
            dividend < divisor
        except:
            return

        remainder = floored_modulo(dividend, divisor)

        # Assert basic modulos equations
        assert modulo_equations(dividend, divisor, remainder)

        # Assert remainder and divisor are same sign
        assert(are_same_sign(remainder, divisor))

        # Assert same output type to one of two inputs type
        assert((type(dividend) is type(remainder)) or (type(divisor is type(remainder))))
        return


def test_floored_modulo():
    construct_test_combinations()
    for values in test_combinations:
        floored_modulo_combination_test(values["dividend"], values["divisor"])


#### Ceiled modulo tests #####

def ceiled_modulo_combination_test(dividend, divisor):
        # We don't test incompatible types operation, as described in README
        try:
            dividend/divisor
            dividend < divisor
        except:
            return

        remainder = ceiled_modulo(dividend, divisor)

        # Assert basic modulos equations
        assert modulo_equations(dividend, divisor, remainder)

        # Assert remainder and divisor are opposite sign (except 0 which it is both positive and negative)
        if remainder > 0:
            assert(divisor <= 0)
        elif remainder < 0:
            assert(divisor >= 0)

        # Assert same output type to one of two inputs type
        assert((type(dividend) is type(remainder)) or (type(divisor is type(remainder))))
        return


def test_ceiled_modulo():
    construct_test_combinations()
    for values in test_combinations:
        ceiled_modulo_combination_test(values["dividend"], values["divisor"])


#### Truncated modulo tests #####

def truncated_modulo_combination_test(dividend, divisor):
        # We don't test incompatible types operation, as described in README
        try:
            dividend/divisor
            dividend < divisor
        except:
            return

        remainder = truncated_modulo(dividend, divisor)

        # Assert basic modulos equations
        assert modulo_equations(dividend, divisor, remainder)

        # Assert remainder and dividend are same sign
        assert(are_same_sign(remainder, dividend))

        # Assert same output type to one of two inputs type
        assert((type(dividend) is type(remainder)) or (type(divisor is type(remainder))))
        return


def test_truncated_modulo():
    construct_test_combinations()
    for values in test_combinations:
        truncated_modulo_combination_test(values["dividend"], values["divisor"])

#### ZeroDivisionError tests #####
def test_zero_division_error():
    with pytest.raises(ZeroDivisionError) as e:
        euclidean_modulo(42, 0)
    with pytest.raises(ZeroDivisionError) as e:
        rounded_modulo(42, 0)
    with pytest.raises(ZeroDivisionError) as e:
        floored_modulo(42, 0)
    with pytest.raises(ZeroDivisionError) as e:
        ceiled_modulo(42, 0)
    with pytest.raises(ZeroDivisionError) as e:
        truncated_modulo(42,0)
