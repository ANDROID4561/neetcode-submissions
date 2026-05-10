class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr=[]
        for n in range(2*len(nums)):
            if n<len(nums):    
                arr.append(nums[n])
            else:
                arr.append(nums[n-len(nums)])
        return arr