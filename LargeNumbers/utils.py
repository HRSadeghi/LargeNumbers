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
from tqdm import tqdm

def simple_gcd(x, y):
    if x < y:
        x, y = y, x
    
    while(y != 0):
        remainder = x % y
        x = y
        y = remainder
    
    return x


def gcdExtended(a, b):
    if a == 0 : 
        return b, 0, 1
            
    gcd, x1, y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd, x, y


def gcd(x, y, _type='simple'):
    if _type == 'simple':
        return simple_gcd(x, y)
    else:
        gcd,_,_, = gcdExtended(x, y)
        return gcd


def string_int_to_very_long_int(input):
    x = np.array(list(input), dtype='int').astype('object')
    i_s = np.arange(len(x))[::-1].astype('object')
    out = np.array([np.sum((10**i_s)*x)], dtype='object')
    return out


def convert_repeating_dec_to_frac(input, gcd_type='extended'):
    input_sign = '-' if input[0] == '-' else ''
    input = input[1:] if input[0] == '-' or input[0] == '+' else input 

    int_dec = input.split('.')
    I = int_dec[0]

    fixed_repeating = int_dec[1].split('R')
    A = fixed_repeating[0]
    P = fixed_repeating[1]

    numerator = string_int_to_very_long_int(I+A+P) - string_int_to_very_long_int(I+A)
    denominator = string_int_to_very_long_int('9'*len(P) + '0'*len(A))
    

    gcd_val = gcd(numerator, denominator, _type=gcd_type)

    numerator = numerator // gcd_val
    denominator =  denominator // gcd_val

    fraction = input_sign + str(numerator[0]) + '/' + str(denominator[0])

    return fraction


def dec_to_frac(input):
    input_sign = '-' if input[0] == '-' else ''
    input = input[1:] if input[0] == '-' or input[0] == '+' else input 

    dec_len = len(input.split('.')[1])
    input = input.replace('.' , '')

    out = number_to_simplest_form(input) + '/' + '1' + '0'*dec_len
    return input_sign + out
    

def number_to_simplest_form(input):
    if type(input) is not str:
        input = str(input)

    if input == '-0' or input == '+0':
        return '0'

    input_sign = '-' if input[0] == '-' else ''
    input = input[1:] if input[0] == '-' or input[0] == '+' else input 
	
    if '/' in input:
        parts = input.split('/')
        s1 = number_to_simplest_form(parts[0])
        s2 = number_to_simplest_form(parts[1])
        if s2 == '1':
            input = s1
        else:
	        input = s1 + '/' + s2



    if '.' in input:
        parts = input.split('.')
        if 'R' in parts[1]:
            R_index = list(parts[1]).index('R')
            part1_set = set(parts[1][R_index:])
            if len(part1_set) == 2:
                if '0' in part1_set and 'R' in part1_set:
                    return input_sign + number_to_simplest_form(parts[0]+ '.' + parts[1][:R_index])
        if len(parts[1]) == 0:
            return input_sign + number_to_simplest_form(input[:-1])
        if len(parts[0]) == 0:
            return input_sign + number_to_simplest_form('0' + input)
        if parts[1][-1] == '0' and 'R' not in parts[1]:
            return  input_sign + number_to_simplest_form(input[:-1])
    if  len(input)>=2:
        if input[0] == '0' and input[1] != '.':
            return  input_sign + number_to_simplest_form(input[1:])
    return input_sign + input



def _sign(x):
    if '-' in x:
        return -1
    if '-' not in x:
        return 1



def to_fraction(input):
    if 'R' in input:
        return to_fraction(convert_repeating_dec_to_frac(input))
    if 'R' not in input and '.' in input:
        return to_fraction(dec_to_frac(input))
    if '/' in input:
        return input.split('/')
    return input, '1'


def _greater(x, y):  # x > y
    x = number_to_simplest_form(x)
    y = number_to_simplest_form(y)

    flag1 = False
    flag2 = False

    if '-' in x:
        flag1 = True
        x = x.replace('-', '0')
    else:
        x = x.replace('+', '1') if '+' in x else '1' + x

    if '-' in y:
        flag2 = True
        y = y.replace('-', '0')
    else:
        y = y.replace('+', '1') if '+' in x else '1' + y

    if flag1 and flag2:
        x, y = y, x

    if '.' in x:
        x_dec_len = len(x.split('.')[1])
    else:
        x_dec_len = 0
    if '.' in y:
        y_dec_len = len(y.split('.')[1])
    else:
        y_dec_len = 0

    x = x.replace('.', '')
    y = y.replace('.', '')
    
    if x_dec_len > y_dec_len:
        y = y + '0'*(x_dec_len - y_dec_len)
        y_dec_len = x_dec_len
    elif x_dec_len < y_dec_len:
        x = x + '0'*(y_dec_len - x_dec_len)
        x_dec_len = y_dec_len

    x_len = len(x)
    y_len = len(y)

    if x_len > y_len:
        y = '0'*(x_len - y_len) + y
    elif x_len < y_len:
        x = '0'*(y_len - x_len) + x

    # method1
    '''x = np.array([int(i) for i in x])
    y = np.array([int(i) for i in y])

    t = (x == y)
    index = np.where(t == False)

    if len(index) == 0:
        return x[0] > y[0]

    x = x[index]
    y = y[index]

    return x[0] > y[0]'''

    # method2
    x = string_int_to_very_long_int(x)
    y = string_int_to_very_long_int(y)
    

    return x > y

    


def _add(x, y):
    if ('R' in x) or ('R' in y) or ('/' in x) or ('/' in y):
        sum = _add_frac(x, y)
        return sum


    if type(x) is str:
        x_sign = -1 if x[0] == '-' else 1
    else:
        x_sign = 1 if x > 0 else -1
    if type(y) is str:
        y_sign = -1 if y[0] == '-' else 1
    else:
        y_sign = 1 if y > 0 else -1

    x = x.replace('-', '').replace('+', '')
    y = y.replace('-', '').replace('+', '')

    x = number_to_simplest_form(x)
    y = number_to_simplest_form(y)

    if '.' in x:
        x_dec_len = len(x.split('.')[1])
    else:
        x_dec_len = 0
    if '.' in y:
        y_dec_len = len(y.split('.')[1])
    else:
        y_dec_len = 0
        

    x = x.replace('.', '')
    y = y.replace('.', '')
    
    if x_dec_len > y_dec_len:
        y = y + '0'*(x_dec_len - y_dec_len)
        y_dec_len = x_dec_len
    elif x_dec_len < y_dec_len:
        x = x + '0'*(y_dec_len - x_dec_len)
        x_dec_len = y_dec_len

    x_len = len(x)
    y_len = len(y)

    if x_len > y_len:
        y = '0'*(x_len - y_len) + y
    elif x_len < y_len:
        x = '0'*(y_len - x_len) + x

    
    # method1
    '''carry = 0
    out = []
    for (i, j) in zip(x[::-1], y[::-1]):
        sum = int(i) + int(j) + carry
        out.append(str(sum%10))
        carry = sum//10

    if carry > 0:
        out = str(carry) + ''.join(out[::-1])
    else:
        out = ''.join(out[::-1])

    if x_dec_len > 0 or y_dec_len > 0:
        out = out[:-x_dec_len] +'.' +out[-x_dec_len:]
    
    return out'''


    # method2
    '''x = np.array([int(i) for i in x])
    y = np.array([int(i) for i in y])

    sum =  x + y
    carry = sum//10

    carry = np.concatenate([carry[1:], np.array([0])]) # shift array
    sum[1:] = sum[1:] % 10
    sum = sum + carry

    carry = sum//10
    carry = np.concatenate([carry[1:], np.array([0])]) # shift array
    sum[1:] = sum[1:] % 10
    sum = sum + carry

    sum = ''.join([str(i) for i in sum])'''

    # method3
    x = string_int_to_very_long_int(x)
    y = string_int_to_very_long_int(y)

    sum = str((x_sign * x + y_sign * y)[0])

    
    if x_sign * y_sign > 0 and x_dec_len > 0:
        if x_dec_len > 0 or y_dec_len > 0:
            sum = sum[:-x_dec_len] + '.' + sum[-x_dec_len:]
    elif x_dec_len > 0:
        sum_sign = '-' if sum[0] == '-' else ''
        sum = sum.replace('-', '')
        if len(sum) < x_dec_len:
            sum = '0.' + ''.join(['0']*(x_dec_len - len(sum))) + sum
        else:
            sum = sum[:-x_dec_len] + '.' + sum[-x_dec_len:]
        
        sum = sum_sign + sum
    
    return number_to_simplest_form(sum)



def _multiply(x, y):
    if ('R' in x) or ('R' in y) or ('/' in x) or ('/' in y):
        prod = _multiply_frac(x, y)
        return prod

    if type(x) is str:
        x_sign = -1 if x[0] == '-' else 1
    else:
        x_sign = 1 if x > 0 else -1
    if type(y) is str:
        y_sign = -1 if y[0] == '-' else 1
    else:
        y_sign = 1 if y > 0 else -1

    x = x.replace('-', '').replace('+', '')
    y = y.replace('-', '').replace('+', '')

    x = number_to_simplest_form(x)
    y = number_to_simplest_form(y)

    if '.' in x:
        x_dec_len = len(x.split('.')[1])
    else:
        x_dec_len = 0
    if '.' in y:
        y_dec_len = len(y.split('.')[1])
    else:
        y_dec_len = 0

    x = x.replace('.', '')
    y = y.replace('.', '')
    
    if x_dec_len > y_dec_len:
        y = y + '0'*(x_dec_len - y_dec_len)
        y_dec_len = x_dec_len
    elif x_dec_len < y_dec_len:
        x = x + '0'*(y_dec_len - x_dec_len)
        x_dec_len = y_dec_len

    x_len = len(x)
    y_len = len(y)

    if x_len > y_len:
        y = '0'*(x_len - y_len) + y
    elif x_len < y_len:
        x = '0'*(y_len - x_len) + x
    

    x = string_int_to_very_long_int(x)
    y = string_int_to_very_long_int(y)


    mul = str((x*y*x_sign*y_sign)[0])

    if x_dec_len > 0 or y_dec_len > 0:
        mul = mul[:-2*x_dec_len] + '.' + mul[-2*x_dec_len:]

    return number_to_simplest_form(mul)





def _divide(x, y, max_dec_num = 100, repeating_form = False, return_frac = False):  # x/y
    if ('R' in x) or ('R' in y) or ('/' in x) or ('/' in y) or return_frac:
        dev = _divide_frac(x, y)
        a, b = to_fraction(dev)
        if return_frac:
            return a + '/' + b
        
        return _divide(a, b, max_dec_num = max_dec_num, repeating_form = repeating_form, return_frac = False)
        

    if type(x) is str:
        x_sign = -1 if x[0] == '-' else 1
    else:
        x_sign = 1 if x > 0 else -1
    if type(y) is str:
        y_sign = -1 if y[0] == '-' else 1
    else:
        y_sign = 1 if y > 0 else -1

    x = x.replace('-', '').replace('+', '')
    y = y.replace('-', '').replace('+', '')

    x = number_to_simplest_form(x)
    y = number_to_simplest_form(y)

    if '.' in x:
        x_dec_len = len(x.split('.')[1])
    else:
        x_dec_len = 0
    if '.' in y:
        y_dec_len = len(y.split('.')[1])
    else:
        y_dec_len = 0

    x = x.replace('.', '')
    y = y.replace('.', '')
    
    if x_dec_len > y_dec_len:
        y = y + '0'*(x_dec_len - y_dec_len)
        y_dec_len = x_dec_len
    elif x_dec_len < y_dec_len:
        x = x + '0'*(y_dec_len - x_dec_len)
        x_dec_len = y_dec_len

    x_len = len(x)
    y_len = len(y)

    if x_len > y_len:
        y = '0'*(x_len - y_len) + y
    elif x_len < y_len:
        x = '0'*(y_len - x_len) + x
    

    x = string_int_to_very_long_int(x)
    y = string_int_to_very_long_int(y)

    if y == 0:
        raise ValueError('The denominator\'s value is zero')
    
    

    int_part = str((x//y)[0]) + '.'
    remainder = x % y
    x = remainder * 10

    dec_part = []
    remainders = []
    remainders_set = set()
    counter = 0
    index = -1

    while(remainder[0] != 0 and counter < max_dec_num):
        counter += 1 
        remainders += [remainder]
        remainders_set.add(remainder[0])
        dec_part += [str((x//y)[0])]
        remainder = x % y
        x = remainder * 10

        if repeating_form:
            if remainder[0] in remainders_set:
                counter = max_dec_num
                index = remainders.index(remainder)


    if index >= 0:
        out = int_part + ''.join(dec_part[:index]) + 'R' + ''.join(dec_part[index:])
    else:
        out = int_part + ''.join(dec_part) 
        out = number_to_simplest_form(out)
        if remainder[0] != 0:
            out += 'L'
    if out != '0':
        out = '-' + out if x_sign*y_sign == -1 else out

    return out
        



def _invert(x, return_frac = True, repeating_form = False, max_dec_num = 100):  # 1/x
    return _divide('1', x, max_dec_num = max_dec_num, repeating_form = repeating_form, return_frac = return_frac)


def _frac_to_dec(x, repeating_form = False, max_dec_num = 100):  # 1/x
    a, b = to_fraction(x)
    return _divide(a, b, max_dec_num = max_dec_num, repeating_form = repeating_form, return_frac = False)
    
def _add_frac(x, y):
    a, b = to_fraction(x)   # x = a/b
    c, d = to_fraction(y)   # y = c/d

    t1 = _multiply(a,d)
    t2 = _multiply(b,c)
    t3 = _multiply(b,d)

    t4 = _add(t1, t2)

    t3_sign = -1 if t3[0] == '-' else 1
    t4_sign = -1 if t4[0] == '-' else 1

    t3 = t3.replace('-', '').replace('+', '')
    t4 = t4.replace('-', '').replace('+', '')

    t3 = string_int_to_very_long_int(t3)
    t4 = string_int_to_very_long_int(t4)


    g = gcd(t3, t4)

    t3 = t3//g
    t4 = t4//g

    t4 *= t3_sign*t4_sign
    
    if t3 != 1: 
        num = number_to_simplest_form(str(t4[0]))
        den = number_to_simplest_form(str(t3[0]))
        return num + '/' + den
    else:
        num = number_to_simplest_form(str(t4[0]))
        return num


def _multiply_frac(x, y):
    a, b = to_fraction(x)   # x = a/b
    c, d = to_fraction(y)   # y = c/d

    t1 = _multiply(a,c)
    t2 = _multiply(b,d)

    t1_sign = -1 if t1[0] == '-' else 1
    t2_sign = -1 if t2[0] == '-' else 1

    t1 = t1.replace('-', '').replace('+', '')
    t2 = t2.replace('-', '').replace('+', '')

    t1 = string_int_to_very_long_int(t1)
    t2 = string_int_to_very_long_int(t2)

    g = gcd(t1, t2)

    t1 = t1//g
    t2 = t2//g

    t1 *= t1_sign*t2_sign

    if t2 != 1: 
        num = number_to_simplest_form(str(t1[0]))
        den = number_to_simplest_form(str(t2[0]))
        return num + '/' + den
    else:
        num = number_to_simplest_form(str(t1[0]))
        return num



def _divide_frac(x, y):
    y_sign = '-' if y[0] == '-' else ''
    y = y.replace('-', '').replace('+', '')
    c, d = to_fraction(y)   # y = c/d

    return _multiply_frac(x, y_sign + d +'/'+c)

