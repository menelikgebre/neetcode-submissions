class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = ""
        
        # Start at index 2 so we can always look 2 steps back
        for i in range(2, len(num)):
            # Check if the current character and the previous two are identical
            if num[i] == num[i-1] == num[i-2]:
                # Grab the 3-character string
                current_window = num[i-2:i+1] # i+1 makes it inclusive of index i
                
                # Lexicographical comparison works perfectly here
                if current_window > max_num:
                    max_num = current_window
                    
        return max_num