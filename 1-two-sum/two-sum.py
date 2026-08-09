class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store the number and its corresponding index
        seen = {}
        
        for index, num in enumerate(nums):
            # Calculate the required complement
            complement = target - num
            
            # If the complement exists in the map, we found the pair
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, store the current number and its index
            seen[num] = index
            
        return []
