class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compare = set()
        for n in nums:
            if n in compare:
                return True 
            else: 
                compare.add(n) 
        return False