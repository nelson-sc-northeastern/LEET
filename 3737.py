class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ret = 0

        cnt = 0

        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                cnt += 1 if nums[j] == target else -1
                if cnt > 0:
                    ret += 1
        

        return ret