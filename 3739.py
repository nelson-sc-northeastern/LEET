class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        prefix = [0] * (N * 2 + 1)
        prefix[N] = 1
        ret = 0
        cnt = N
        presum = 0
        for i in range(N):
            if nums[i] == target:
                presum += prefix[cnt]
                cnt += 1
                prefix[cnt] += 1
            else:
                cnt -= 1
                presum -= prefix[cnt]
                prefix[cnt] += 1
            ret += presum

        return ret 