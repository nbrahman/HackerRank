def checkNextString(s):
    i = len(s) - 1
    while i > 0 and s[i - 1] >= s[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(s) - 1
    while s[j] <= s[i - 1]:
        j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]

    s[i:] = s[len(s) - 1: i - 1: -1]
    return True

q = int(input().strip())
for a0 in range(q):
    s = list(input().strip())
    if checkNextString(s):
        print("".join(s))
    else:
        print('no answer')