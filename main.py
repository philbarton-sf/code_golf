import sys

v = [[1], [9, 5, 4, 1], [9, 5, 4, 1], [9, 5, 4, 1]]
s = [['M'], ['CM', 'D', 'CD', 'C'], ['XC', 'L', 'XL', 'X'], ['IX', 'V', 'IV', 'I']]
with open(sys.argv[1], 'r') as f:
    l = f.readline().strip()
    while l != '':
        r = ''
        for i, c in enumerate(l.zfill(4)):
            d = int(c)
            if d == 0:
                continue
            for j in v[i]:
                if d >= j:
                    r += s[i][v[i].index(j)]
                    d -= j
        print(l, r)
        l = f.readline().strip()
