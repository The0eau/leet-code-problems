"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Initialize two pointers at the start and end of the array
        left = 0
        right = len(nums) - 1
        
        # Continue searching while the search space is valid
        while left <= right:
            # Find the middle index
            # (In some languages, left + (right - left) // 2 is used to prevent integer overflow, 
            # but Python handles arbitrarily large integers automatically)
            mid = (left + right) // 2
            
            # If we found the target, return its index
            if nums[mid] == target:
                return mid
                
            # If the middle element is less than the target, 
            # the target must be in the right half. Ignore the left half.
            elif nums[mid] < target:
                left = mid + 1
                
            # If the middle element is greater than the target,
            # the target must be in the left half. Ignore the right half.
            else:
                right = mid - 1
                
        # Target was not found in the array
        return -1

# Test block to verify the code runs correctly
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.search(nums1, target1)}\n")
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.search(nums2, target2)}\n")

    # Test case 3 (Extra: Array with one element)
    nums3 = [5]
    target3 = 5
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.search(nums3, target3)}")