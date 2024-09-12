#metode Tabel
import math
a = -0.9
b = 0.1
u = 0
n = 100
h = (b-a)/n
xi = -0.9
def fx(o):
    q = math.exp(o) + o
    return q
while u < n and fx(xi)*fx(xi+h) > 0:
    u += 1
    xi = -0.9 + h*u
x = xi
print(f"nilai tabel: {x}")
print(f"jumlah perulangan: {u}")
print(f"nilai f(x): {fx(x)}")

#metode Biseksi
a = -0.9
b = 0.1
u = 0
n = 100
#e = 5*(10**-5)
e = 0.00005
def fx(o):
    q = math.exp(o) + o
    return q
def avg(a,b):
    x = (a + b)/2
    return x
r = b - a
while r > e and u < n:
    p = avg(a,b) 
    l = fx(p)*fx(a)
    if l < 0:
        b = p
        print(b)
    else:
        a = p
        print(a)
    r = b - a
    u += 1
t = avg(a,b)
print(f"nilai hasil biseksi: {t}")
print(f"jumlah perulangan: {u}")
print(f"f(x): {fx(t)}")

#metode regulafalsi

a = -0.9
b = 0.1
e = 5*(10**-5)
#e = 0.00005
u = 0
n = 100
def err(q):
    if q < 0:
        e = -q
    else:
        e = q
    return e
def fin(a,b):
    x = (fx(b)*a - fx(a)*b)/(fx(b) - fx(a))
    return x
w = err(fx(fin(a,b)))
while w > e and u < n:
    p = fin(a,b)
    if fx(a)*fx(p) < 0:
        b = p
        print(b)
    else:
        a = p
        print(a)
    w = err(fx(fin(a,b)))
    u += 1
t = fin(a,b)
print(f"nilai hasil regulfalsi = {t}")
print(f"jumlah perulangan: {u}")
print(f"f(x): {fx(t)}")