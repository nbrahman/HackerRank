def is_matched(expression):
    l = []
    for c in expression:
        if c == '{' or c == '[' or c == '(':
            l.append(c)
        elif c == '}' or c == ']' or c == ')':
            if len(l) > 0:
                c2 = l.pop()
                if (c2 != '{' and c == '}') or (c2 != '[' and c == ']') or (c2 != '(' and c == ')'):
                    return False
            else:
                return False
    if len(l) == 0:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
