from itertools import combinations_with_replacement

def BRUH_ITERATOR(L, r, count = 1, cur = None):
    if count == 1:
        cur = tuple()
        L = tuple(L)
    for i in range(len(L)):
        if count == r:
            yield cur + (L[i],)
        else:
            for e in BRUH_ITERATOR(L[i:], r, count + 1, cur + (L[i],)):
                yield e


L = [1, 2, 3, 4]
L = 'abcde'
R = 3

for el in combinations_with_replacement(L, R):
    print(*el, sep = '', end = '\t')
print()
for el in BRUH_ITERATOR(L, R):
    print(*el, sep = '', end = '\t')
