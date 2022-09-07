# Large Numbers

In this repository, a project has been implemented that allows you to perform the four basic operations of addition, subtraction, multiplication and division on large and very large numbers.

## Installation

To use the model, just clone the project and change the path to the corresponding directory.

```
git clone https://github.com/HRSadeghi/LargeNumbers.git

cd LargeNumbers
```

## Usage

The easiest way to use this library is as follows,

```python
from LargeNumber import LargeNumber, largeNumberFormat

a = LargeNumber('125763678041689463179.45761346709461437894')
b = LargeNumber('-746011541145.47464169741644487000085')

# Negation
print(-a)
print(-b)

# Addition and Subtraction
print(a+b)
print(a-b)
print(-a+b)

# Multiplication
print(a*b)

# Division
largeNumberFormat.precision = 100
largeNumberFormat.return_repeating_form = False
largeNumberFormat.return_fracation = False

print(a/b)

```

<br/>
You can also define one of the numbers as a string,

```python
from LargeNumber import LargeNumber, largeNumberFormat

a = LargeNumber('125763678041689463179.45761346709461437894')
b = '-746011541145.47464169741644487000085'

# Ops
print(a+b)
print(a-b)
print(a*b)
print(a/b)



a = '125763678041689463179.45761346709461437894'
b = LargeNumber('-746011541145.47464169741644487000085')

# Ops
print(a+b)
print(a-b)
print(a*b)
print(a/b)
```
