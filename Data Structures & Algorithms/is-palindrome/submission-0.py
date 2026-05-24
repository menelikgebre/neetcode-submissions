class Solution:
    def isPalindrome(self, s: str) -> bool:
        # length will always be one 
        # watch out for upper/lower case, special chars, spaces
        # Was it a car or a cat I saw?"

        # one idea, clean up the whitespaces, special chars, etc...
            # compare cleaned version to reverse and return bool
        # clean_s = ""
        # for char in s:
        #     if char.isalnum():
        #         clean_s += char.lower()
        # return clean_s == reversed(clean_s)

        # other option if we dont want sorting algos time complexitiy 
            # maybe two pointers 

        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()

        p1,p2 = 0, len(clean_s) -1
        while p1 < p2:
            if clean_s[p1] != clean_s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True