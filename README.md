# Modulos

Simple pure Python library implementing modulo operations

![Tests](https://github.com/samhanic/modulos/actions/workflows/tests.yml/badge.svg)

## Purpose

Modulo operation implement remainder of a division, based on this simple formula, with an integer quotient:
$$ dividend = divisor * quotient + remainder$$

However, as quotient can be any integer, multiple definitions of modulo can outputs different result, depending of the implementation used. This can be seen with math.fmod which explicitely says that it may have different output from % symbol.

This library fixes that by adding 5 different implementations of the operation :

* Euclidean modulo (output smallest positive remainder. Probably the one you're looking for if you're coming from mathematical background)
* Rounded modulo (output closest to zero remainder)
* Floored modulo (output remainder with same sign as divisor)
* Truncated modulo (outputs remainder with same sign as dividend)
* Ceiled modulo (outputs remainder with opposite sign as divisor)

This may be useful for (but not limited to):

* Port code from another language implementing different definition of modulo
* Use specific mathematical properties of a definition (especially euclidean or rounded)
* Use same mathematical definition for integers and floats values

## Example

```python
from modulos.modulos import euclidean_modulo, rounded_modulo, floored_modulo, ceiled_modulo, truncated_modulo

print(f"{euclidean_modulo(5,3)=}")
print(f"{rounded_modulo(5,3)=}")
print(f"{floored_modulo(5,3)=}")
print(f"{truncated_modulo(5,3)=}")
print(f"{ceiled_modulo(5,3)=}")

```

### Why would I use these library when Python math library already contains some of its functions ?

Contrary to math.fmod (for truncated modulo) and math.remainder (for rounded modulo), this library keeps same type as inputs (if both are same type).
This can be particularly interesting when working with Decimal library, to avoid rounding issues.

Be aware that this means this library does not cast values from the types they were in. Generally it does not cause any issue, but if your dividend and divisor types does not support division between them, you will have to manually perform the cast. This is for example the case between Decimal built-in library and Numpy types. It does also mean it does not correct roundness issues within float.

## Contributions

You're welcome to contribute to the source code by opening issue or pull request ;)  

A basic test setup have been implemented, here are the steps to run the unit tests on a linux environment:

```bash
cd modulos
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -e .
pip install -r requirements_dev.txt
pytest
```
