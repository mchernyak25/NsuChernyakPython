N, K, M = map(int, input().split())
if N <= K:
    r = 2
else:
    if (2 * N) % K == 0:
        r = (2 * N) // K
    else:
        r = (2 * N) // K + 1
print(r * M)