import sys

def digit_hangman(c):
    word = c[0]
    test = c[1:]
    d = {0: ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']}
    for index_a, a in enumerate(test):
        l = list(d[index_a])
        for index_b, b in enumerate(word):
            if a[0] == b:
                l[index_b] = a[0]
        if l == d[index_a]:
            l.append(a[0])
        d[index_a+1] = l
    last_row = d[5][0:12]
    score = 12 - last_row.count('_')
    d[6] = [score]
    # Print Session
    ans = ''
    for i in d.keys():
        for a in d[i]:
            ans += str(a)
            ans += ' '
        ans += '\n'
    print(ans)   

if __name__ == "__main__":
    s_input = [line.rstrip().split() for line in sys.stdin]
    digit_hangman(s_input)