class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        output = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_map and hash_map[diff] != i:
                j = hash_map.get(diff,0)
                output.append(j)
                output.append(i)
                return output
            hash_map[nums[i]]=i
        return output