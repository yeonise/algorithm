def solution(commands):
    merged = [[(i, j) for j in range(51)] for i in range(51)]
    content = [['EMPTY'] * 51 for _ in range(51)]

    def update1(r, c, value):
        mr, mc = merged[r][c]
        content[mr][mc] = value

    def update2(value1, value2):
        for i in range(1, 51):
            for j in range(1, 51):
                if content[i][j] == value1:
                    content[i][j] = value2

    def merge(r1, c1, r2, c2):
        mr1, mc1 = merged[r1][c1]
        mr2, mc2 = merged[r2][c2]

        if (mr1, mc1) != (mr2, mc2):
            for i in range(1, 51):
                for j in range(1, 51):
                    if merged[i][j] == (mr2, mc2):
                        merged[i][j] = (mr1, mc1)

        if content[mr1][mc1] == 'EMPTY' and content[mr2][mc2] != 'EMPTY':
            content[mr1][mc1] = content[mr2][mc2]

    def unmerge(r, c):
        mr, mc = merged[r][c]
        tmp = content[mr][mc]

        for i in range(1, 51):
            for j in range(1, 51):
                if merged[i][j] == (mr, mc):
                    merged[i][j] = (i, j)
                    content[i][j] = 'EMPTY'

        content[r][c] = tmp

    answer = []

    def print_cell(r, c):
        mr, mc = merged[r][c]
        answer.append(content[mr][mc])

    for command in commands:
        command = command.split()

        if command[0] == 'UPDATE':
            if len(command) == 4:
                update1(int(command[1]), int(command[2]), command[3])
            else:
                update2(command[1], command[2])
        elif command[0] == 'MERGE':
            merge(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == 'UNMERGE':
            unmerge(int(command[1]), int(command[2]))
        else:
            print_cell(int(command[1]), int(command[2]))

    return answer
