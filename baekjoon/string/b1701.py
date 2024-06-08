# Cubeditor
# suffix array와 LCP(Longest Common Prefix) array를 이용해 해결할 수 있습니다.
string = input()

length = len(string)
suffixes = sorted([(string[i:], i) for i in range(length)])  # 모든 접미사를 생성하고 사전순으로 정렬합니다.
suffix_array = [suffix[1] for suffix in suffixes]  # 각 접미사의 시작 인덱스를 저장한 배열을 생성합니다.

# ex. "banana"
# suffixes: ("a", 5), ("na", 4), ("ana", 3), ("nana", 2), ("anana", 1), ("banana", 0)
# after sorting: ("a", 5), ("ana", 3), ("anana", 1), ("banana", 0), ("na", 4), ("nana", 2)
# suffix_array: [5, 3, 1, 0, 4, 2]
# 정렬해서 풀었을 때 가장 효과적인 이유 알아보기

rank = [0] * length
lcp = [0] * length

for index, suffix in enumerate(suffix_array):  # 각 접미사에 대한 순위를 계산합니다.
    rank[suffix] = index  # rank: [3, 2, 5, 1, 4, 0]

h = 0

for i in range(length):
    if rank[i] > 0:  # 인덱스가 0인 경우 0 - 1 계산에서 인덱스 범위 에러가 발생하기 때문에 작성합니다.
        j = suffix_array[rank[i] - 1]
        # 만약 i가 1인 경우 rank[i] = 2, i부터 시작하는 "anana"의 순위는 2입니다.
        # j는 2순위보다 하나 높은 1순위의 시작 인덱스가 됩니다. 즉, j = 3입니다.

        # 인접한 접미사 쌍 간의 가장 긴 공통 접두사를 계산합니다.
        # 1 + 0 < 6 and 3 + 0 < 6 and "a" == "a", h = 1
        # 1 + 1 < 6 and 3 + 1 < 6 and "n" == "n", h = 2
        # 1 + 2 < 6 and 3 + 2 < 6 and "a" == "a", h = 3
        while i + h < length and j + h < length and string[i + h] == string[j + h]:
            h += 1

        lcp[rank[i]] = h

        if h > 0:
            h -= 1

# LCP: [1, 3, 0, 0, 2, 0]
print(max(lcp))  # LCP 배열에서 가장 큰 값을 찾습니다. 이 값이 가장 긴 반복 부분 문자열의 길이입니다.

# 시간 복잡도
# python 1s: 10,000,000
# N = 5,000
# suffix array 구축: O(N log N) = 400,000
# LCP array 구축: O(N) = 5,000
# 가장 긴 공통 접두사 찾기: O(N) = 5,000
