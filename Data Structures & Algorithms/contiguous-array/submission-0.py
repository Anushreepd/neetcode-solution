class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        prefix_map = {0: -1}

        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            if prefix_sum in prefix_map:
                length = i - prefix_map[prefix_sum]
                max_length = max(max_length, length)
            else:
                prefix_map[prefix_sum] = i
        return max_length
        pass
