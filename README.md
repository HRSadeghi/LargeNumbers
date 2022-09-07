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
largeNumberFormat.return_fracation = False

print(a/b)

```

In the above code snippet, because the number of digits for the division operation may be very large, so a maximum can be defined for it using `largeNumberFormat.precision`.


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



<br/>
You can also use numbers as fractions,

```python
from LargeNumber import LargeNumber, largeNumberFormat

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

print(a+b)
print(a-b)
print(a*b)
print(a/b)
##


```