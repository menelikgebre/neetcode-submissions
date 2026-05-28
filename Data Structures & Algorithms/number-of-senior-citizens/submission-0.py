class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # lots of information in this list of strings
            # always at least one element, length always 15
                # 10 (phone) + 1 (gender) + 2 (age) + 2 (seat)
        # this function only job relates to age and returning count of > 60

        # we can safely assume we only care about indices element[11:13]
            # index 11, 12
        
        count = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                count += 1
        
        return count