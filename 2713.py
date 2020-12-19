CODEC = {
    ' ': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
    'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

T = int(input())

for i in range(T):
    TC = [x for x in input().split()]

    R, C = int(TC[0]), int(TC[1])
    msg = ' '.join(TC[2:])

    result = [[0 for j in range(C)] for k in range(R)]
    binary = []

    for alpha in msg:
        binary += [int(x) for x in f'{CODEC[alpha]:05b}']

    print(binary)
    row, col = 0, 0
    minR, minC, maxR, maxC = 0, 0, R-1, C-1
    horizon, toggle_row, toggle_col = True, True, True

    for bin in binary:
        print('result[{}][{}]={}, minR{} minC{} maxR{} maxC{}'.format(col, row, bin, minR, minC, maxR, maxC))
        result[col][row] = bin

        if horizon:
            if (toggle_row and row==maxR) or (not toggle_row and row==minR):
                if toggle_row:
                    maxR -= 1
                else:
                    minR += 1

                horizon = not horizon
                toggle_row = not toggle_row

        else:
            if (toggle_col and col == maxC) or (not toggle_col and col == minC):
                if toggle_col:
                    maxC -= 1
                else:
                    minC += 1

                horizon = not horizon
                toggle_col = not toggle_col

        if horizon:
            row = row+1 if toggle_row else row-1

        else:
            col = col+1 if toggle_col else col-1

    print(result)
