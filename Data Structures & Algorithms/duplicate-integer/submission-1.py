class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_value=list(set(nums))
        if len(n_value)<len(nums):
            return True
        return False

        