######## a) x_k = x_(k-1)*x**2/(2n(2n-1))
########### x_0 = x**2/2 k >= 0



def gen_a (x, k):
    x = x**2/2
    yield x
    for i in range(2, k+1):
        x*= (x**2/(2*i*(2*i-1)))
        yield x

x = 2
k = 5
for i in gen_a(x, k):
    print (f'a) {i}')



######### b) P_k = P_(k-1)*(1 + 1/k**2)
############ k >= 1 P_1 = 2


def gen_b(k):
     P = 2
     yield P
     for i in range (2, k+1):
         P *= (1 + 1/(i**2))
         yield P


q = 2
for i in gen_b(q):
    P = i
print(f'b) {P}')



############ c) D_n = (a+b)D_(n-1) - ab(D_(n-2))
############### D_0 = 1 D_1 = a+b


def gen_c(n, a, b):
    d_0 = 1
    yield d_0
    d_1 = a + b
    yield d_1
    for i in range(2, n+1):
        d = (a + b)*d_0 - a*b*d_1
        d_0 = d_1
        d_1 = d
        yield d

a = 1
b = 2
n = 3
for i in gen_c(n, a, b):
    print(f'c) {i}')



############ d) S_n = S_(n-1) + a_n/2**n
############### a_1 = a_2 = a_3 = 1
############### a_k = a_(k-1) + a_(k-3)


def gen_d_a(k):
    a1 = 1
    yield a1
    a2 = 1
    yield a2
    a3 = 1
    yield a3
    for i in range(4, k+1):
        a = a3 - a1
        a1 = a2
        a2 = a3
        a3 = a
        yield a



def gen_d_S(n):
    S = 0.5
    yield S
    for i in range(2, n):
        for u in gen_d_a(n):
            a = u
        for e in range(2, n+1):
            S += a/2**e
            yield S

w = 3

for i in gen_d_S(w):
    S = i

print(f'd) {S}')



############ e) T_k = T_(k-1)*x**2*(2k-1)/(2k+1)
############### k >= 1 T_0 = 2x


def gen_e(x, n):
    T = 2*x
    yield T
    for i in range(2, n+1):
        T *= x**2*(2*k-1)/(2*k+1)
        yield T

r = 2
t = 4

for i in gen_e(r, t):
    T = i
print(f'T={T}')