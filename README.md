<!---
Copyright 2022 Hamidreza Sadeghi. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Large Numbers

In this repository, a library has been provided that allows you to perform the four basic operations of addition, subtraction, multiplication and division on large and very large numbers. We tried to make this library as fast and efficient as possible.

Note: In this library, powering is not supported yet, but it will be supported in the next versions.



## Installation

To install, you can use `pip` as follows.
<br/>

```
pip install LargeNumbers
```

<br/>

To install from the repository, just clone the project, change the path to the corresponding directory and then install lib using `pip`.

<br/>

```
git clone https://github.com/HRSadeghi/LargeNumbers.git

cd LargeNumbers

pip install .
```

## Usage

The easiest way to use this library is as follows,
<br/>

```python
from LargeNumbers.LargeNumber import LargeNumber, largeNumberFormat

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
largeNumberFormat.return_fracation = False

print(a/b)

```

<br/>




<br/>

In the above code snippet, because the number of digits for the division operation may be very large, so a maximum can be defined for it using `largeNumberFormat.precision`. If the number of digits appearing in the division process is more than the number of digits allocated for `largeNumberFormat.precision`, then a letter `L` appears at the end of the number (this letter has no effect in further calculations).

```python
from LargeNumbers.LargeNumber import LargeNumber, largeNumberFormat

largeNumberFormat.precision = 2

a = LargeNumber('1')
b = LargeNumber('7')

print(a/b)

```


<br/>

You can also define one of the numbers as a `string`, `int` or `float`,

```python
from LargeNumbers.LargeNumber import LargeNumber, largeNumberFormat

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
print()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
```


<br>

But if the input is a `string`, you cannot negate it first.
<br>

```python

from LargeNumbers.LargeNumber import LargeNumber, largeNumberFormat

a = '125763678041689463179.45761346709461437894'
b = LargeNumber('-746011541145.47464169741644487000085')

print(-a+b)

# In this case, you will encounter the following error
"""
TypeError: bad operand type for unary -: 'str'
"""

```

<br/>

You can also give input numbers as fractions,

<br/>

```python
from LargeNumbers.LargeNumber import LargeNumber, largeNumberFormat

a = LargeNumber('1/2')
b = LargeNumber('-3/14')

# Ops (return the result as a fraction)
largeNumberFormat.return_fracation = True

print(a+b)
print(a-b)
print(a*b)
print(a/b)
##

# Ops (return the result as a decimal)
largeNumberFormat.precision = 5
largeNumberFormat.return_fracation = False

print()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
##


```

<br/>

It is also possible to give numbers as input and get the output as a fraction or non-fraction,
<br/> 

```python
from LargeNumbers.LargeNumber import LargeNumber, largeNumberFormat

a = LargeNumber('2.142')
b = LargeNumber('-3/14')

# Ops (return the result as a fraction)
largeNumberFormat.return_fracation = True

print(a+b)
print(a-b)
print(a*b)
print(a/b)
##

a = LargeNumber('1.134')
b = LargeNumber('-1.57')

# Ops (return the result as a decimal)
largeNumberFormat.return_fracation = True

print()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
##


```


## Recurring decimal (repeating decimal)
Numbers such as $\dfrac{1}{3}$, $\dfrac{1}{7}$ and similar numbers do not have a finite decimal representation. Therefore, we are facing a problem to perform division in these numbers. But these numbers can be shown in periodic form. As a result, $\dfrac{1}{3}$ can be represented by $0.\overline{3}$ and $\dfrac{1}{7}$ by $0.\overline{142857}$. 

Here, the letter R is used to show the beginning of the period. Therefore, we represent a number like $0.\overline{3}$ with `0.R3`, a number like $0.\overline{7}$ with `0.R7` and a number like $0.12\overline{42}$ with `0.12R42`.


According to this way of representation, we can apply the four operations of addition, subtraction, multiplication and division on the same representation.
 

```python
from LargeNumbers.LargeNumber import LargeNumber, largeNumberFormat

largeNumberFormat.return_repeating_form = True
largeNumberFormat.return_fracation = False
largeNumberFormat.precision = 30


a = LargeNumber('0.R81')
b = LargeNumber('0.134R1')

# Ops 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
##


a = LargeNumber('0.12R81')
b = LargeNumber('0.665')

# Ops 
print()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
##


a = LargeNumber('1/7')
b = LargeNumber('0.665')

# Ops 
print()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
##
```


In the above code snippet, `largeNumberFormat.return_repeating_form` specifies whether the number is in recurring (repeating) form or not. If the number of digits in the periodic display exceeds the number of digits dedicated to the `largeNumberFormat.precision`, the number will not be displayed recurringly and an `L` will appear at the end of the number (this letter has no effect in further calculations).

```python
from LargeNumbers.LargeNumber import LargeNumber, largeNumberFormat

largeNumberFormat.return_repeating_form = True
largeNumberFormat.return_fracation = False
largeNumberFormat.precision = 6

a = LargeNumber('1')
b = LargeNumber('7')

print(a/b)

largeNumberFormat.precision = 5

print()
print(a/b)
```