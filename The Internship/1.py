import sys

def sorting_acronyms(c):
    output = []
    upper_case = ''
    upper_char = [chr(i) for i in range(65,91)]
    for i in c:
        for j in i:
            if j in upper_char:
                upper_case += j
        output.append(upper_case)
        upper_case = ''
    output = list(filter(None, output))
    output.sort(key = len, reverse= True)
    #print session
    for i in output:
        print(i)


if __name__ == "__main__":
    s_input = [line.rstrip() for line in sys.stdin]
    sorting_acronyms(s_input)
