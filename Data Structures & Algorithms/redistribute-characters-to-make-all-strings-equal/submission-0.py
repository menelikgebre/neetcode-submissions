from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # is it possible to make every val in words equal?
            # nothing we can do when keys dont match
                # find the min len(word)
                # make
            # but if keys matched and freq just off then whats the formula''

           # ["abcz","aabczz","bc"]

           # all have "bc" together
           # then whats left? 
            # a - aazzzz - __
            # total we got
                # 3 spots
                # 3 as
                # 6 zs
            # reordering only possible if
                # each char freq % len(words) == 0
            
            s = "".join(words)
            count = Counter(s)

            for key, freq in count.items():
                if freq % len(words) != 0:
                    return False
            return True

