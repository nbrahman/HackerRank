# #!/bin/python3

def findPattern(G, P):
    patRows = len(P)
    patCols = len(P[0])

    for y, rowGrid in enumerate(G[:1-patRows]):
        newG = G[y:]

        pos = rowGrid.find(P[0])
        while pos != -1:
            for rowPattern, grid_row in zip(P, newG):
                grid_sub = grid_row[pos:pos+patCols]
                if grid_sub != rowPattern:
                    break
            else:
                return 'YES'

            pos = rowGrid.find(P[0], pos + 1)

    return 'NO'


t = int(input().strip())
for a0 in range(t):
    R,C = map(int,input().strip().split(' '))
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = map(int, input().strip().split(' '))
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
    print(findPattern(G, P))
