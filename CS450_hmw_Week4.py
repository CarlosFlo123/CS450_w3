import array
#Ex1__________________________________________________
def if_function(condition, true_result, false_result):
  if condition:
    return true_result
  else:
    return false_result

#if_function(True, 2, 3)
#if_function(False, 2, 3)
#if_function(3==2, 3+2, 3-2)
#if_function(3>2, 3+2, 3-2)


#Ex2___________________________________________________
def sum_odd(limit):
  c = 0;
  while(limit != 0):
    if (limit % 2 == 1):
      c = c + limit
    limit = limit - 1
  return c

#sum_odd(6)
#sum_odd(7)


#Ex3__________________________________________________
def minFour(a, b, c, d):
  if (a < b and a < c and a < d):
    return True
  return False
def minThree(a, b, c):
  if (a < b and a < c):
    return True
  return False
def foo(a, b, c, d):
  smallest = a
  smaller = b
  if (minFour(a, b, c, d)):
    smallest = a
    if (minThree(b, c, d)):
      smaller = b
    elif (minThree(c, d, b)):
      smaller = c
    elif (minThree(d, b, c)):
      smaller = d
  elif (minFour(b, c, d, a)):
    smallest = b
    if (minThree(c, d, a)):
      smaller = c
    elif (minThree(d, a, c)):
      smaller = d
    elif (minThree(a, c, d)):
      smaller = a
  elif (minFour(c, d, a, b)):
    smallest = c
    if (minThree(d, a, b)):
      smaller = d
    elif (minThree(a, b, d)):
      smaller = a
    elif (minThree(b, d, a)):
      smaller = b
  elif (minFour(d, a, b, c)):
    smallest = d
    if (minThree(a, b, c)):
      smaller = a
    elif (minThree(b, c, a)):
      smaller = b
    elif (minThree(c, a, b)):
      smaller = c
  return (smallest**2 + smaller**2)

#foo(1, 2, 3, 4)
#foo(-3, 1, 5, 6)


#Ex4__________________________________________________
def comp(a, b, c):
  if (a - b == c) or (b - c == a) or (c - a == b):
    return True
  return False
def df(a, b, c):
  if (comp(a, b, c) or comp(b, a, c)):
    return True
  return False

#df(2,5,3)
#df(-2,3,5)
#df(-5,-3,-2)
#df(-2, 3, -5)
#df(2, 3, -5)
#df(10, 6, 4)
#df(10, 6, 3)


#Ex5__________________________________________________
def lrgst_factor(m):
  tmp = m - 1
  if (m == 5 or m == 3 or m == 2):
    return m
  while(tmp != 0):
    if (m % tmp == 0):
      return tmp
    tmp -= 1
  return tmp

#lrgst_factor(15)
#lrgst_factor(80)
#lrgst_factor(3)


#Ex6__________________________________________________
def pfct_num(m):
  sum_factors = 0
  tmp = 1
  while (tmp != (m/2 + 1)):
    if (m % tmp == 0):
      sum_factors += tmp
    tmp += 1
  if (sum_factors == m):
    return True
  else:
    return False

#pfct_num(6)
#pfct_num(8)
#pfct_num(28)


#Ex7__________________________________________________
def get_Digits(x):
  digits = 1
  while (x > 9):
    x /= 10
    digits += 1
  return digits
def same_ord(a, b):
  if(get_Digits(a) == get_Digits(b)):
    return True
  return False

#same_ord(50,70)
#same_ord(50,100)
#same_ord(1000,100000)


#Ex8__________________________________________________
def double_5(n):
  con = 0
  while(n > 1):
    if(int(n) % 10 == 5):
      con += 1
    else:
      con = 0
    if (con == 2):
      return True
    n /= 10
  return False

#double_5(5)
#double_5(55)
#double_5(550055)
#double_5(12345)
#double_5(50505050)


#Ex9__________________________________________________
def uniq_digits(x):
  digits = []
  while(x > 1):
    if (int(x%10) not in digits):
      digits.append(int(x%10))
    x /= 10
  return len(digits)

#uniq_digits(8675309)
#uniq_digits(1313131)
#uniq_digits(13173131)
#uniq_digits(100000)
#uniq_digits(101)
