"""
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort the intervals based on the starting value (index 0) of each interval
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If the merged list is empty, or if the current interval does NOT overlap 
            # with the previous one (current start > previous end), append it directly.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # Otherwise, there is an overlap. 
            # We merge the current and previous intervals by updating the end time 
            # of the previous interval to the maximum end time of the two.
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged

# Test block to verify the code runs correctly
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Input: intervals = {intervals1}")
    print(f"Output: {solution.merge(intervals1)}\n")
    
    # Test case 2
    intervals2 = [[1, 4], [4, 5]]
    print(f"Input: intervals = {intervals2}")
    print(f"Output: {solution.merge(intervals2)}\n")
    
    # Test case 3
    intervals3 = [[4, 7], [1, 4]]
    print(f"Input: intervals = {intervals3}")
    print(f"Output: {solution.merge(intervals3)}")