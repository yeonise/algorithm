bingo = []
table = [0] * 26

for _ in range(5):
    bingo.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        table[bingo[i][j]] = (i, j)

col = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
row = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
left_diagonal = {(0, 0): 0, (1, 1): 0, (2, 2): 0, (3, 3): 0, (4, 4): 0}
right_diagonal = {(0, 4): 0, (1, 3): 0, (2, 2): 0, (3, 1): 0, (4, 0): 0}

count = 0

for line in range(5):
    host = list(map(int, input().split()))

    for index, number in enumerate(host):
        r, c = table[number]
        col[c] += 1
        row[r] += 1

        if col[c] >= 5:
            count += 1
            col[c] = -5
        if row[r] >= 5:
            count += 1
            row[r] = -5

        if table[number] in left_diagonal:
            left_diagonal[table[number]] += 1

            if sum(left_diagonal.values()) >= 5:
                count += 1
                left_diagonal[(0, 0)] = -5

        if table[number] in right_diagonal:
            right_diagonal[table[number]] += 1

            if sum(right_diagonal.values()) >= 5:
                count += 1
                right_diagonal[(0, 4)] = -5

        if count >= 3:
            print(line * 5 + index + 1)
            exit()
