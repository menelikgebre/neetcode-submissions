class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the total preferences: e.g., {0: count_of_0s, 1: count_of_1s}
        counts = [students.count(0), students.count(1)]
        
        for sandwich in sandwiches:
            # If we still have students who prefer this sandwich, serve them
            if counts[sandwich] > 0:
                counts[sandwich] -= 1
            else:
                # If no one left wants this top sandwich, the line stalls forever
                break
                
        # The remaining students are the ones we couldn't serve
        return sum(counts)