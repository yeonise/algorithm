# 소형 기관차
num_carriages = int(input())
num_passengers = [0] + list(map(int, input().split()))
max_carriages = int(input())

# i개의 소형 기관차가 j개의 객체까지 최대로 끌었을 때 운송할 수 있는 최대 손님 수를 저장한다
dp = [[0] * (num_carriages + 1) for _ in range(4)]
prefix_sum = [0] * (num_carriages + 1)

# 누적합을 구한다
for i in range(1, num_carriages + 1):
    prefix_sum[i] = prefix_sum[i - 1] + num_passengers[i]

for i in range(1, 4):
    for j in range(max_carriages, num_carriages + 1):
        # dp[i][j - 1] : 현재 소형 기관차를 사용하지 않고 이전 객차까지의 최대 손님 수
        # dp[i - 1][j - max_carriages] : 이전 소형 기관차들이 이전 객차까지 운송한 최대 손님 수
        # prefix_sum[j] - prefix_sum[j - max_carriages] : 현재 객차까지 총 max_carriages개의 객차에 타고 있는 손님 수의 합
        # 즉 현채 소형 기관차를 타느냐 타지 않느냐 이렇게 2가지 경우를 비교하여 값을 저장한다
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - max_carriages] + prefix_sum[j] - prefix_sum[j - max_carriages])

print(dp[3][num_carriages])
