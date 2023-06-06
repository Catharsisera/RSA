import random
from sympy import *

def prime_pq(a,b):
    p = random.randint(a, b)
    q = random.randint(a, b)
    if p == q:
        q = random.randint(a, b)
    if p % 2 == 0:
        p += 1
    if q % 2 == 0:
        q += 1
    while not(isprime(p) and isprime(q)):
        if not(isprime(p)):
            p += 2
        if not(isprime(q)):
            q += 2

    return(p,q)

def nod(a,b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def extendEvklid(a, b):
    if a == 0:
        return b, 0, 1
    mod, x1, y1 = extendEvklid(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return mod, x, y

def invE(e, Fn):
    gcd, x, y = extendEvklid(e, Fn)
    if gcd == 1:
        return (x % Fn + Fn) % Fn
    else:
        return -1

def gen_key():
    p, q = prime_pq(1000, 2000)
    N = p * q
    Fn = (p - 1) * (q - 1)
    e = random.randint(1, Fn)

    if e % 2 == 0:
        e += 1
    while not isprime(e):
        if nod(e, Fn) != 1:
            e += 2
        else:
            break

    res = invE(e, Fn)
    if res != -1:
        d = res

    print('p = ', p, 'q = ', q, 'e =', e, 'd = ', d)

    return {
        'encrypt_key': [e, N],
        'decrypt_key': [d, N]
    }

def encrypt(M, arr):
    c = (M ** arr[0]) % arr[1]
    return c

def decrypt(c, arr):
    m = (c ** arr[0]) % arr[1]
    return m

openText = ['M','i','t']
bintext = []
for i in openText:
    bintext.append(ord(i))
    print(type(i))
print(bintext)

keys = gen_key()
print(keys)

arr = []
for i in bintext:
    arr.append(encrypt(i, keys['encrypt_key']))
print('Shipher text: ', arr)

arr2 = []
result = []
for i in arr:
    arr2.append(decrypt(i, keys['decrypt_key']))
print(arr2)
for i in arr2:
    result.append(chr(i))
print(result)
print('Open text: ', ''.join(result))
