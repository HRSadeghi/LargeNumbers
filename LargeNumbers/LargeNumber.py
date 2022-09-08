#Copyright 2022 Hamidreza Sadeghi. All rights reserved.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.



import numpy as np
from LargeNumbers.LargeNumberFormat import LargeNumberFormat
from LargeNumbers.utils import gcd, _add, string_int_to_very_long_int, convert_repeating_dec_to_frac
from LargeNumbers.utils import dec_to_frac, number_to_simplest_form, to_fraction, _multiply
from LargeNumbers.utils import _divide, _invert, _frac_to_dec



largeNumberFormat = LargeNumberFormat()

class LargeNumber(object):
    def __init__(self, value):
        self.value = number_to_simplest_form(str(value).replace('L', '').replace('+', '').strip())
        self.larger_than_precision = True if 'L' in str(value) else False


    def __repr__(self):
        if self.larger_than_precision:
            return self.value + 'L'
        return self.value
    
    def __str__(self):
        if self.larger_than_precision:
            return self.value + 'L'
        return self.value

    def __len__(self):
        return len(self.value)

    def __add__(self, x):
        if type(x) == LargeNumber:
            sum = _add(self.value, x.value)
        elif type(x) == float or int or str:
            sum = _add(self.value, str(x))
        else:
            raise ValueError('The data type {} is not supported!'.format(type(x)))

        if ('/' in sum) and (not largeNumberFormat.return_fracation):
           sum = _frac_to_dec(sum, repeating_form=largeNumberFormat.return_repeating_form, max_dec_num=largeNumberFormat.precision)
        elif largeNumberFormat.return_fracation:
            sum = _divide(sum,
                          '1',
                          max_dec_num = largeNumberFormat.precision,
                          repeating_form = largeNumberFormat.return_repeating_form,
                          return_frac = largeNumberFormat.return_fracation)
        return LargeNumber(sum)

    def  __radd__(self, x):
        return self.__add__(x)

    
    def __rsub__(self, x):
        self.value =  self.value.replace('-', '')  if '-' in self.value else '-' + self.value
        out = self.__add__(x)
        self.value =  self.value.replace('-', '')  if '-' in self.value else '-' + self.value
        return out

    def __sub__(self, x):
        out = self.__rsub__(x)
        out.value =  out.value.replace('-', '')  if '-' in out.value else '-' + out.value
        return out

    def __mul__(self, x):
        if type(x) == LargeNumber:
            _mul = _multiply(self.value,  x.value)
        elif type(x) == int or float or str:
            _mul = _multiply(self.value,  str(x))            
        else:
            raise ValueError('The data type {} is not supported!'.format(type(x)))

        _mul =  _divide(_mul,
                        '1',
                        max_dec_num = largeNumberFormat.precision,
                        repeating_form = largeNumberFormat.return_repeating_form,
                        return_frac = largeNumberFormat.return_fracation)

        return LargeNumber(_mul)


    def __rmul__(self, x):
        return self.__mul__(x)


    def __truediv__(self, x):
        if type(x) == LargeNumber:
            return LargeNumber(_divide(self.value,
                                       x.value,
                                       max_dec_num = largeNumberFormat.precision,
                                       repeating_form = largeNumberFormat.return_repeating_form,
                                       return_frac = largeNumberFormat.return_fracation))
        elif type(x) == int or float or str:
            return LargeNumber(_divide(self.value,
                                       str(x),
                                       max_dec_num = largeNumberFormat.precision,
                                       repeating_form = largeNumberFormat.return_repeating_form,
                                       return_frac = largeNumberFormat.return_fracation))
        else:
            raise ValueError('The data type {} is not supported!'.format(type(x)))


    def __rtruediv__(self, x):
        if type(x) == LargeNumber:
            return LargeNumber(_divide(x.value,
                                       self.value,
                                       max_dec_num = largeNumberFormat.precision,
                                       repeating_form = largeNumberFormat.return_repeating_form,
                                       return_frac = largeNumberFormat.return_fracation))
        elif type(x) == int or float or str:
            return LargeNumber(_divide(str(x),
                                       self.value,
                                       max_dec_num = largeNumberFormat.precision,
                                       repeating_form = largeNumberFormat.return_repeating_form,
                                       return_frac = largeNumberFormat.return_fracation))
        else:
            raise ValueError('The data type {} is not supported!'.format(type(x)))
    
    def __floordiv__(self, x):
        if type(x) == LargeNumber:
            return LargeNumber(_divide(self.value,
                                       x.value,
                                       max_dec_num = 1,
                                       repeating_form = False,
                                       return_frac = False).split('.')[0].replace('L',''))
        elif type(x) == int or float or str:
            return LargeNumber(_divide(self.value,
                                       str(x),
                                       max_dec_num = 1,
                                       repeating_form = False,
                                       return_frac = False).split('.')[0].replace('L',''))
        else:
            raise ValueError('The data type {} is not supported!'.format(type(x)))

    
    def __rfloordiv__(self, x):
        if type(x) == LargeNumber:
            return LargeNumber(_divide(x.value,
                                       self.value,
                                       max_dec_num = 1,
                                       repeating_form = False,
                                       return_frac = False).split('.')[0].replace('L',''))
        elif type(x) == int or float or str:
            return LargeNumber(_divide(str(x),
                                       self.value,
                                       max_dec_num = 1,
                                       repeating_form = False,
                                       return_frac = False).split('.')[0].replace('L',''))
        else:
            raise ValueError('The data type {} is not supported!'.format(type(x)))
            
    def __eq__(self, x):
        if type(x) == LargeNumber:
            a, b = to_fraction(x.value)
            a_sign = -1 if '-' in a else 1
            a = a.replace('-', '').replace('+', '')
        elif type(x) == int or float or str:
            a, b = to_fraction(str(x))
            a_sign = -1 if '-' in a else 1
            a = a.replace('-', '').replace('+', '')
        else:
            raise ValueError('The data type {} is not supported!'.format(type(x)))
        c, d = to_fraction(self.value)
        c_sign = -1 if '-' in c else 1
        c = c.replace('-', '').replace('+', '')


        a = string_int_to_very_long_int(a)
        b = string_int_to_very_long_int(b)
        c = string_int_to_very_long_int(c)
        d = string_int_to_very_long_int(d)

        g1 = gcd(a, b)
        a = a//g1
        b = b//g1

        g2 = gcd(c, d)
        c = c//g2
        d = d//g2

        return (a_sign*a == c_sign*c and b == d)[0]

    
    def __gt__(self, x):
        if type(x) == LargeNumber:
            a, b = to_fraction(x.value)
            a_sign = -1 if '-' in a else 1
            a = a.replace('-', '').replace('+', '')
        elif type(x) == int or float or str:
            a, b = to_fraction(str(x))
            a_sign = -1 if '-' in a else 1
            a = a.replace('-', '').replace('+', '')
        else:
            raise ValueError('The data type {} is not supported!'.format(type(x)))
        c, d = to_fraction(self.value)
        c_sign = -1 if '-' in c else 1
        c = c.replace('-', '').replace('+', '')


        a = string_int_to_very_long_int(a)
        b = string_int_to_very_long_int(b)
        c = string_int_to_very_long_int(c)
        d = string_int_to_very_long_int(d)

        g1 = gcd(a, b)
        a = a//g1
        b = b//g1

        g2 = gcd(c, d)
        c = c//g2
        d = d//g2

        p1 = _multiply(str(a[0]), str(d[0]))
        p2 = _multiply(str(c[0]), str(b[0]))

        p1 = string_int_to_very_long_int(p1)
        p2 = string_int_to_very_long_int(p2)

        return (a_sign*p1 < c_sign*p2)[0]



    def __ge__(self, x):
        return self.__gt__(x) or self.__eq__(x)

    def __le__(self, x):
        return not self.__gt__(x)

    def __lt__(self, x):
        return not self.__ge__(x)

    def __neg__(self):
        value_sign = '-' if '-' in self.value else ''
        new_val = self.value.replace('-', '').replace('+', '')
        neg_val = new_val if value_sign == '-' else '-' + new_val
        neg_number = LargeNumber(neg_val)
        return neg_number

    
    
        
