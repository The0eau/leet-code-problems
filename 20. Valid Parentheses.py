"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Hash map for keeping track of mappings. 
        # The key is the closing bracket, the value is the matching opening bracket.
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise, assign a dummy value '#' to fail the match
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the stack's top element, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack
                stack.append(char)
                
        # If the stack is empty, we successfully matched everything.
        # If it's not empty, there are unclosed brackets left.
        return not stack

# Test block to verify the code runs correctly
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "()"
    print(f"Input: s = '{s1}'")
    print(f"Output: {solution.isValid(s1)}\n")
    
    # Test case 2
    s2 = "()[]{}"
    print(f"Input: s = '{s2}'")
    print(f"Output: {solution.isValid(s2)}\n")
    
    # Test case 3
    s3 = "(]"
    print(f"Input: s = '{s3}'")
    print(f"Output: {solution.isValid(s3)}\n")
    
    # Test case 4
    s4 = "([])"
    print(f"Input: s = '{s4}'")
    print(f"Output: {solution.isValid(s4)}\n")
    
    # Test case 5
    s5 = "([)]"
    print(f"Input: s = '{s5}'")
    print(f"Output: {solution.isValid(s5)}")