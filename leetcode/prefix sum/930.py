# Binary Subarrays With Sum
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        prefix_sum = 0
        counter = {0: 1}

        for num in nums:
            prefix_sum += num
            # prefix_sum - goal이 counter에 존재하면, 그것이 목표합을 가지는 부분 배열의 시작점이 되므로 그 수만큼 결과에 더한다
            result += counter.get(prefix_sum - goal, 0)
            counter[prefix_sum] = counter.get(prefix_sum, 0) + 1

        return result
