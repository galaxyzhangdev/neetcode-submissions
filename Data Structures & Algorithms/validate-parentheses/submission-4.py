class Solution:
    def isValid(self, s: str) -> bool:
            # Dictionary to hold the matching pairs
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to hold the opening brackets
        stack = []

        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # If the character is a closing bracket
                # Pop the top element of the stack (if it's empty, use a dummy value '#')
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # After processing all characters, check if the stack is empty
        return not stack