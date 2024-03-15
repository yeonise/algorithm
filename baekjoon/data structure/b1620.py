# 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int, sys.stdin.readline().strip().split())

dict_num = {}
dict_name = {}

for i in range(N):
    name = sys.stdin.readline().strip()
    dict_num[i + 1] = name
    dict_name[name] = i + 1

for _ in range(M):
    key = sys.stdin.readline().strip()
    if key.isdigit():
        print(dict_num[int(key)])
    else:
        print(dict_name[key])
