class Solution:
    def maxScore(self, s: str) -> int:
        # Start by counting all 1s on the right side
        ones_right = s.count('1')
        zeros_left = 0
        max_score = 0
        
        # Loop until len(s) - 1 because the right substring cannot be empty
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1
                
            # Calculate the score at this split point
            max_score = max(max_score, zeros_left + ones_right)
            
        return max_score