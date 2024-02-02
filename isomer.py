A = [1]
b = []
a = []
n = int(input())
for m in range(n):
    tmp = 0
    for i in range(m//2+1):
        if i*2 != m:
            tmp += A[i]*A[m-i]
    b.append(tmp)
    tmp = 0
    for i in range(m+1):
        tmp += A[i]*b[m-i]
    for i in range(m//2+1):
        if 3*i != m:
            tmp -= A[i]*A[i]*A[m-2*i]
    tmp //= 3
    a.append(tmp)
    for i in range(m//2+1):
        if 3*i != m:
            tmp += A[i] * (A[i] + 1) // 2 * A[m - 2 * i]
    if m % 3 == 0:
        tmp += A[m // 3] * (A[m // 3] + 1) * (A[m // 3] + 2) // 6
    A.append(tmp)
B = 0
for i in range(1, n//2+1):
    if i*2 != n:
        B += A[i] * A[n - i]
if n % 2 == 0:
    B += A[n // 2] * (A[n // 2] - 1) // 2
m = n-1
C = 0
for i in range(m+1):
    C += A[i] * a[m - i]
for i in range(m//2+1):
    C -= A[i] * A[i] * b[m - 2 * i]
for i in range(m//3+1):
    if 4*i != m:
        C += A[i] * A[i] * A[i] * A[m - 3 * i]
C //= 4
for i in range(m//2+1):
    C += A[i] * (A[i] + 1) // 2 * b[m - 2 * i]
for i in range(m//3+1):
    if 4*i != m:
        C -= A[i] * (A[i] + 1) // 2 * A[i] * A[m - 3 * i]
if m % 2 == 0:
    for i in range(m//4+1):
        if 4*i != m:
            C += A[i] * (A[i] + 1) // 2 * A[m // 2 - i] * \
                (A[m // 2 - i] + 1) // 2
for i in range(m//3+1):
    if 4*i != m:
        C += A[i] * (A[i] + 1) * (A[i] + 2) // 6 * A[m - 3 * i]
if m % 4 == 0:
    C += A[m // 4] * (A[m // 4] + 1) * (A[m // 4] + 2) * \
        (A[m // 4] + 3) // 24
print(C-B)