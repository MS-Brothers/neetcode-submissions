class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for index , val in enumerate(nums):
            com = target - val
            if com in dic:
                return [dic[com],index]
            dic[val]=index    