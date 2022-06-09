# Modulos

Simple pure Python library implementing modulo operations

## Purpose

Modulo operation implement remainder of a division, based on this simple formula, with an integer quotient:
$$ dividend = divisor * quotient + remainder$$

However, as quotient can be any integer, multiple definitions of modulo can outputs different result, depending of the implementation used. This can be seen with math.fmod which explicitely says that it may have different output from % symbol.

This library fixes that by adding 5 different implementations of the operation :

* Euclidean modulo (output smallest positive remainder)
* Rounded modulo (output closest to zero remainder)
* Floored modulo (output remainder with same sign as divisor)
* Truncated modulo (outputs remainder with same sign as dividend)
* Ceiled modulo (outputs remainder with opposite sign as divisor)

This may be useful for (but not limited to):

* Port code from another language implementing different definition of modulo
* Use specific mathematical properties of a definition (especially euclidean or rounded)
* Use same mathematical definition for integers and floats values

Note that this library does not correct roundness issues.

### Why would I use these library when Python math library already contains some of its functions ?

Contrary to math.fmod (for truncated modulo) and math.remainder (for rounded modulo), this library keeps the type of inputs (when identical).
This can be particularly interesting when working with Decimal library, to avoid rounding issues.

## Conributions

You can contribute to the source code by opening issue or pull request.
